import soundfile, librosa, sys
import numpy as np

# def conv(x): return np.clip(np.log10(x + 1) / 5, 0, 1)
def conv(x): return np.clip(0.021 * (x + 1e-10) ** (1 / 3), 0, 1)

def expand(x: np.ndarray, mult: int):
        x_next = np.concatenate((x[1 : ], [0.0]))
        interp = np.arange(mult, dtype = float) / mult
        return (x[ : , None] * (1 - interp) + x_next[ : , None] * interp).ravel()

def main(input: str, output: str):
    audio, sr = librosa.load(input, sr = None, mono = True)
    print(f'Size: {audio.size}')

    n_fft = 2048
    hop_length = 512

    S = librosa.stft(audio, n_fft = n_fft, hop_length = hop_length, window = 'hann')
    P = np.abs(S) ** 2
    fqs = librosa.fft_frequencies(sr = sr, n_fft = n_fft)

    mask1 = (fqs >= 20) & (fqs <= 1000)
    mask2 = (fqs >= 1500) & (fqs <= 4000)

    bpt1 = (P * mask1[..., np.newaxis]).sum(axis = 0)
    bpt2 = (P * mask2[..., np.newaxis]).sum(axis = 0)

    bdbt1 = conv(bpt1) * 0.9
    bdbt2 = conv(bpt2) * 2.0

    soundfile.write(output + '1.wav', expand(bdbt1, hop_length), sr)
    soundfile.write(output + '2.wav', expand(bdbt2, hop_length), sr)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage:\n'
              'python <fname>.py input.wav output')
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])