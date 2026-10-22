import numpy as np
from pedalboard import Pedalboard, Gain, LowShelfFilter, HighShelfFilter, PeakFilter
import soundfile as sf
import sounddevice as sd
from PIL import Image, ImageDraw, ImageFont
import librosa, os, struct, time, platform

def clamp(x, l, r): return l if x < l else r if x > r else x
def sequal(x): return '' if x is None else f'{x:.1f}'

AUDIO_PATH = "res"
TEXT_PATH = "res"
FRQ_PATH = "res"
IM_SRC_PATH = "image_src"
IM_DST_PATH = "res"
os.makedirs(AUDIO_PATH, exist_ok = True)
os.makedirs(TEXT_PATH, exist_ok = True)
os.makedirs(FRQ_PATH, exist_ok = True)
os.makedirs(IM_DST_PATH, exist_ok = True)

positions = ['top_left', 'top_right', 'bottom_left', 'bottom_right', 'center']

class OtoEntry:
    '''
    Oto.ini file entry formatting.

    :param alias: Name of the voice unit
    :param offset: Starting point of sound (ms)
    :param consonant: Also called Fixed part, length of the part not to be stretched (ms)
    :param cutoff: Ending point of sound (ms)
    :param preutt: Aligning point of sound (ms)
    :param overlap: Length of the crossfading part (ms)
    '''
    def __init__(self, alias: str = None, offset: float = None, consonant: float = None,
                                   cutoff: float = None, preutt: float = None, overlap: float = None):
        self.alias = alias or ''
        self.offset = sequal(offset)
        self.consonant = sequal(consonant)
        self.cutoff = sequal(cutoff)
        self.preutt = sequal(preutt)
        self.overlap = sequal(overlap)

    def as_name(self, alt_alias: str = None):
        'Deep copies the instance wit only the alias altered.'
        alt = OtoEntry(self.alias if alt_alias is None else alt_alias)
        alt.offset = self.offset
        alt.consonant = self.consonant
        alt.cutoff = self.cutoff
        alt.preutt = self.preutt
        alt.overlap = self.overlap
        return alt

    def __str__(self) -> str:
        return f'{self.alias},{self.offset},{self.consonant},{self.cutoff},{self.preutt},{self.overlap}'

    def __mod__(self, other: str):
        if '%' not in self.alias: return self.as_name()
        return self.as_name(self.alias % other)

class Tc:
    '''
    The Utility class for soundbank i/o, calculation, and formatting.

    :param sr: Sample rate (Hz)
    :param bf: Base frequency, all waveforms generated will take this frequency (Hz)
    :param frq_pad: The content to pad into .frq files, anything beyond 16 bytes will be truncated (string)
    :param save_frq: Whether to calculate and save its frq table when saving audio. For faster debug only
    '''
    def __init__(self, sr: int = 44100, bf: float = 220.0, frq_pad: str = '', save_frq: bool = True):
        self.sample_rate: int = sr
        self.base_freq: float = bf
        self.save_count: int = 0
        self.oto_entries: dict[str, list[OtoEntry]] = {}
        self.frq_pad: bytes = bytes(frq_pad, 'utf-8')
        if len(self.frq_pad) > 16: self.frq_pad = self.frq_pad[ : 16]
        elif len(self.frq_pad) < 16: self.frq_pad = self.frq_pad.ljust(16, b'\0')
        self.save_frq_flag = save_frq

    def ttos(self, time: float) -> int:
        'Time to sample count conversion by sample rate'
        return int(time * self.sample_rate)
    
    def stot(self, sample: int) -> float:
        'Sample count to time conversion by sample rate'
        return sample / self.sample_rate
    
    def _idv(self, time: float, k: int, modulator: np.ndarray = None) -> np.ndarray:
        'The time variable for waveforms'
        # To make it consistent, we use arange instead of linspace
        x0 = np.arange(l := self.ttos(time)) / self.sample_rate * k * self.base_freq
        if modulator is None or np.all(modulator == 0.0): # Skip modulation if there is none
            return x0
        dl = modulator.size - l
        if dl >= 0: # modulator longer than time
            x0 += modulator[ : l] / (2 * np.pi)
        else: # shorter
            x0 += np.pad(modulator, (0, dl), 'edge') / (2 * np.pi)
        return x0
    
    def sine(self, time: float, k: int, modulator: np.ndarray = None) -> np.ndarray:
        'Sine wave. Can have a multiplier on frequency and/or a modulator to add to time variable'
        return np.sin(2 * np.pi * self._idv(time, k, modulator))
    
    def saw(self, time: float, k: int, modulator: np.ndarray = None) -> np.ndarray:
        'Sawtooth wave. Can have a multiplier on frequency and/or a modulator to add to time variable'
        return (2 * self._idv(time, k, modulator)) % 2 - 1
    
    def triangle(self, time: float, k: int, modulator: np.ndarray = None, duty: float = 0.5) -> np.ndarray:
        'Triangle wave. Can have a multiplier on frequency and/or a modulator to add to time variable'
        x0 = self.saw(time, k, modulator)
        return np.where(x0 <= 2 * duty - 1, (x0 + 1) / duty - 1, (x0 - 1) / (duty - 1) - 1)
    
    def square(self, time: float, k: int, modulator: np.ndarray = None, duty: float = 0.5) -> np.ndarray:
        'Square wave. Can have a multiplier on frequency and/or a modulator to add to time variable'
        x0 = self.saw(time, k, modulator)
        return np.where(x0 <= 2 * duty - 1, 1, -1)
    
    def noise(self, time: float) -> np.ndarray:
        'White noise. **Does not** have frequency multiplier or modulator'
        return np.random.random(self.ttos(time)) * 2 - 1
    
    def interp(self, time: float, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        'Linear interpolation between two sequences'
        return np.interp(np.arange(self.ttos(time)) / self.sample_rate, x, y)

    def shift_add(self, base: np.ndarray, additive: np.ndarray, dtime: float = 0.0) -> np.ndarray:
        'Shift-and-add operation. Result will be the same length as base, and out-of-bound elements in additive will be seen as 0'
        if additive is None: return base.copy()
        res = base.copy()
        dsamp = self.ttos(dtime)
        lb = max(0, dsamp)
        ub = min(base.size, dsamp + additive.size)
        if lb < ub:
            res[lb : ub] += additive[lb - dsamp : ub - dsamp]
        return res

    def save(self, seq: np.ndarray, fname: str, oto_entry: OtoEntry, oto_dupe_no_alias: bool = False):
        '''Save a sound file and adds its oto entry into object buffer. Also calculates and saves its frq file as well by default.
        Only use when sound files and oto entries is one-to-one. If there are multiple oto entries on one sound file, please
        use `save_sep` instead. If `oto_dupe_no_alias == True` and oto entry is provided with an alias,
        then a copy without alias is also created.'''
        self.save_sep(seq, fname, [oto_entry], oto_dupe_no_alias)

    def save_sep(self, seq: np.ndarray, fname: str, oto_entries: OtoEntry | list[OtoEntry], oto_dupe_no_alias: bool = False):
        '''Save a sound file and adds its oto entries into object buffer. Also calculates and saves its frp file as well by default.
        If `oto_dupe_no_alias == True` and oto entry is provided with an alias, then a copy without alias is also created.'''
        try:
            sf.write(os.path.join(AUDIO_PATH, fname + '.wav'), seq, self.sample_rate)
            if isinstance(oto_entries, OtoEntry): oto_entries = [oto_entries]
            if oto_dupe_no_alias:
                oto_dupe: list[OtoEntry] = []
                for oto in oto_entries:
                    if oto.alias: oto_dupe.append(oto.as_name(''))
                oto_entries = oto_entries + oto_dupe
            if fname in self.oto_entries: self.oto_entries[fname] += oto_entries
            else: self.oto_entries[fname] = oto_entries
            self.save_count += 1
        except Exception as E:
            print(f"[Error] Cannot save {AUDIO_PATH}\\{fname}.wav!")
            print(E)
        else:
            print(f"[Info] {AUDIO_PATH}\\{fname}.wav saved successfully, {len(oto_entries)} oto entries added.")
            if self.save_frq_flag: self._calc_and_save_frq(seq, fname + '_wav')

    def _calc_and_save_frq(self, seq: np.ndarray, fname: str, frame_length: int = 512, hop_length: int = 256, cheat: bool = True):
        'Calculates, encodes and saves a soundfile\'s frequency-amplitude table, aka. frq file'
        # Frequency table is conveniently calculated by LibRosa for us
        freq_table, _, _ = librosa.pyin(seq, fmin = 60, fmax = 2000, sr = self.sample_rate,
                                       frame_length = frame_length, hop_length = hop_length, fill_na = 0)
        freq_average = np.mean(freq_table[freq_table >= 60]) if np.any(freq_table >= 60) else 0.0
        if cheat and 400 <= freq_average <= 480: # How the hell did pyin get a 440Hz
            freq_table /= 2
            freq_average /= 2

        # But we have to do RMS ourselves
        seq_len = seq.size
        table_len = freq_table.size
        required_len = (table_len - 1) * hop_length + frame_length
        if table_len < required_len:
            pad_width = (required_len - seq_len) // 2 + 1
            seq = np.pad(seq, pad_width, 'constant', constant_values = 0)
        rms_table = 32767 * np.array([
            np.sqrt(np.mean(seq[_idx * hop_length : _idx * hop_length + frame_length] ** 2))
            for _idx in range(table_len)
        ])

        # Then we stuff the precious data into binary file
        try:
            with open(os.path.join(FRQ_PATH, fname + '.frq'), 'wb') as frq_file:
                # File Header / Magic Number
                frq_file.write(b'FREQ0003')
                # Hop length, 256 by default
                frq_file.write(struct.pack('<I', hop_length))
                # Average frequency
                frq_file.write(struct.pack('<d', freq_average))
                # 16 bytes of padding, we can add extra info
                frq_file.write(self.frq_pad)
                # Data amount
                frq_file.write(struct.pack('<I', table_len))
                # Now it's time for our tables
                for freq, amp in zip(freq_table, rms_table):
                    frq_file.write(struct.pack('<dd', freq, amp))
        except Exception as E:
            print(f'[Error] Cannot save {FRQ_PATH}\\{fname}.frq!')
            print(E)
        else:
            print(f'[INFO] {FRQ_PATH}\\{fname}.frq saved successfully.')

    def preview(self, seq: np.ndarray, ident: str = None, conlog: bool = True):
        'Plays a sound defined by an array. Shares a sample rate with this instance'
        try:
            if not ident: ident = '<unnamed>'
            if conlog: print(f'[Info] Playing sound {ident}...', end = '')
            output_stream = sd.OutputStream(self.sample_rate, channels = 1)
            with output_stream:
                output_stream.write(seq.astype(np.float32))
        except Exception as E:
            print(f'\n[Error] Cannot play sound {ident}!')
            print(E)
        else:
            if conlog: print(' Done')

    def save_oto(self, encoding = 'utf-8'):
        'Saves all oto entries collected by this instance'
        if not self.oto_entries:
            print('[Warning] No oto entry found.')
            return
        try:
            oto_count = 0
            with open(os.path.join(TEXT_PATH, 'oto.ini'), 'w', encoding = encoding) as oto_file:
                for ident in sorted(self.oto_entries):
                    oto_alias_exist: set[str] = set()
                    for entry in self.oto_entries[ident]:
                        if entry.alias in oto_alias_exist:
                            print(f'[Warning] Multiple oto entries with alias {entry.alias} in file {ident}.wav. Only the first entry will be kept.')
                        else:
                            oto_alias_exist.add(entry.alias)
                            oto_file.write(ident + '.wav=' + entry.__str__() + '\n')
                            oto_count += 1
        except Exception as E:
            print(f'[Error] Cannot save {TEXT_PATH}\\oto.ini!')
            print(E)
        else:
            print(f'[Info] Saved {TEXT_PATH}\\oto.ini with {oto_count} entries successfully.')

    def alarm(self):
        'Used as a fast indicator, you can call this after the main function finishes'
        for i in range(4):
            self.preview(self.sine(0.25, i + 1), 'ALERT', False)

    def make_info(self, info_dict: dict):
        'Takes a dict and saves its entries seperately in character.txt and character.yaml. Processes the image and portrait if told to'
        try:
            char_txt_file = open(os.path.join(TEXT_PATH, 'character.txt'), 'w', encoding = 'utf-8')
            char_yaml_file = open(os.path.join(TEXT_PATH, 'character.yaml'), 'w', encoding = 'utf-8')
            for key, value in info_dict.items():
                match key:
                    case 'name' | 'author':
                        char_txt_file.write(f'{key}={value}\n')
                        char_yaml_file.write(f'{key}: {value}\n')
                    case 'localized_names':
                        char_yaml_file.write('localized_names:\n')
                        for lang, lang_name in value.items():
                            char_yaml_file.write(f'  {lang}: {lang_name}\n')
                    case 'text_file_encoding' | 'voice' | 'version' | 'web' | 'default_phonemizer':
                        char_yaml_file.write(f'{key}: {value}\n')
                    case 'image' | 'portrait':
                        char_txt_file.write(f'{key}={key}.png\n')
                        if key == 'portrait':
                            char_yaml_file.write(f'portrait: {key}.png\n')
                            char_yaml_file.write(f'portrait_opacity: {value['opacity']:.2f}\nportrait_height: {value['height']}\n')
                        im_src_fname = value['base']
                        if 'overlay' in value:
                            im_text_prop = value['overlay']
                            im_text: str = im_text_prop['text'] \
                                           .replace('{t}', f'{int(time.time())}') \
                                           .replace('{s}', f'{platform.system()} {platform.release()} {platform.version()}')
                            self._make_image(im_src_fname, f'{key}.png', im_text, im_text_prop['color'],
                                             im_text_prop['pos'], im_text_prop['size'])
                        else:
                            self._make_image(im_src_fname, f'{key}.png', enable = False)
                    case 'extra':
                        char_txt_file.write(value)
                    case _:
                        print(f'[Warning] Unknown key "{key}" will be ignored.')
        except Exception as E:
            print('[Error] Cannot create or write into description files!')
            print(E)
        else:
            print('[Info] Description files created.')
        finally:
            char_txt_file.close()
            char_yaml_file.close()

    def _make_image(self, fname_src: str, fname_dst: str = 'unnamed', text: str = 'No text',
                    color: tuple[int] = (0, 0, 0), pos: str = 'top_left', size: float = 12, *, enable: bool = True):
        'Reads an image, adds (or doesn\'t add) a text and saves it.'
        im = Image.open(os.path.join(IM_SRC_PATH, fname_src))
        if not enable: # Do not add text, and copy it right away
            im.save(os.path.join(IM_DST_PATH, fname_dst))
            return
        if pos not in positions: raise ValueError(f'Invalid text position: {pos}')
        align = 'left' if 'left' in pos else 'right' if 'right' in pos else 'center'
        w, h = im.size
        im_draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('lucon.ttf', size)
        _, _, tw, th = im_draw.multiline_textbbox((0, 0), text, font, align = align)
        im_draw.text(((0 if align == 'left' else (w - tw) if align == 'right' else (w - tw) / 2),
                      (0 if 'top' in pos else (h - th) if 'bottom' in pos else (h - th) / 2)),
                     text, color, font, align = align)
        im.save(os.path.join(IM_DST_PATH, fname_dst))

    def _dbg_print_oto(self):
        for k, v in self.oto_entries.items():
            print(k, '->', v)

    def _dbg_plot(self, t: np.ndarray, y: np.ndarray | list[np.ndarray]):
        'Plots several curves for debug purpose. Also serves as a breakpoint.'
        import matplotlib.pyplot as plt
        if isinstance(y, np.ndarray): plt.plot(t, y)
        else:
            for y_ in y: plt.plot(t, y_)
        plt.show()
        exit(322122547)

if __name__ == '__main__':
    print('This is a utility module, run other files instead!')
    Tc().alarm()