from tc_utils import *

def generate():
    '''
    Generates the entire English C+V soundbank. Should and only be called once.
    The notations mainly follows the ARPAbet.

    The variable prefixes are as followes:
    - v_ variables are standalone vowels and nasals, and diphthongs;
    - c_ variables are standalone consonants;
    - m_ variables are connecting vowels or diphones;
    - s_ variables are complete syllables and are ready to export;
    - x_ variables are for extra sounds;
    - oto_ variables are, obviously, oto entries.
    '''

    start_time = time.time()

    t = 1.0
    base_freq = 220.0
    sample_rate = 44100

    tc = Tc(sample_rate, base_freq, '\0Tcb b1.0 EnC+V')
    tvar = np.linspace(0.0, t, int(t * sample_rate), False)

    # Skip flags
    skip_vowels = False
    skip_diphthongs = False
    skip_consonants = False
    skip_extras = False

    # === Vowels and nasals ===

    vowel_env = (1 - np.exp(-27 * tvar) - np.exp(27 * (tvar - t))) * (0.75 + np.exp(-15 * tvar))
    vowel_filters = Pedalboard([
        PeakFilter(220, -20, 220 / 40),
        PeakFilter(660, -15, 660 / 30),
        PeakFilter(1500, -7.5, 660 / 720),
        Gain(5)
    ])

    if True:
        v_aa = 0.31 * tc.sine(t, 4, 1.2 * tc.sine(t, 1)) \
            + 0.014 * tc.sine(t, 12, 6 * tc.sine(t, 1)) \
            + 0.005 * tc.sine(t, 19, 3 * tc.sine(t, 1)) \
            + 0.001 * tc.sine(t, 26, 2.4 * tc.sine(t, 1, 4 * tc.sine(t, 1)))
        v_aa = vowel_filters(v_aa, sample_rate)

        v_ae = 0.27 * tc.sine(t, 6, 2.5 * tc.sine(t, 1)) \
            + 0.02 * tc.sine(t, 16, 7 * tc.sine(t, 1)) \
            + 0.004 * tc.sine(t, 25, 2 * tc.sine(t, 1)) \
            + 0.001 * tc.sine(t, 36, 3 * tc.sine(t, 1, 5 * tc.sine(t, 1)))
        v_ae = vowel_filters(v_ae, sample_rate)

        v_ah = 0.3 * tc.sine(t, 5, 2 * tc.sine(t, 1)) \
            + 0.02 * tc.sine(t, 15, 8 * tc.sine(t, 1)) \
            + 0.01 * tc.sine(t, 21, 3 * tc.sine(t, 1)) \
            + 0.004 * tc.sine(t, 26, 4 * tc.sine(t, 1, 8 * tc.sine(t, 1)))
        v_ah = vowel_filters(v_ah, sample_rate)

        v_ao = 0.31 * tc.sine(t, 4, 1.4 * tc.sine(t, 1)) \
            + 0.014 * tc.sine(t, 13, 8 * tc.sine(t, 1)) \
            + 0.005 * tc.sine(t, 20, 3 * tc.sine(t, 1)) \
            + 0.001 * tc.sine(t, 26, 2.4 * tc.sine(t, 1, 4 * tc.sine(t, 1)))
        v_ao = vowel_filters(v_ao, sample_rate)

        v_ax = 0.31 * tc.sine(t, 2, 2 * tc.sine(t, 1)) \
            + 0.06 * tc.sine(t, 7, 1.6 * tc.sine(t, 1)) \
            + 0.005 * tc.sine(t, 20, 2.7 * tc.sine(t, 1)) \
            + 0.002 * tc.sine(t, 36, 2 * tc.sine(t, 1, 5 * tc.sine(t, 1)))
        v_ax = vowel_filters(v_ax, sample_rate)

        v_eh = 0.2 * tc.sine(t, 2, 2.5 * tc.sine(t, 1)) \
            + 0.06 * tc.sine(t, 16, 4.5 * tc.sine(t, 1)) \
            + 0.006 * tc.sine(t, 32, 1.7 * tc.sine(t, 1)) \
            + 0.0025 * tc.sine(t, 45, 4 * tc.sine(t, 1, 4 * tc.sine(t, 1)))
        v_eh = vowel_filters(v_eh, sample_rate)

        v_er = 0.31 * tc.sine(t, 2, 1.4 * tc.sine(t, 1)) \
            + 0.06 * tc.sine(t, 6, 1.4 * tc.sine(t, 1)) \
            + 0.005 * tc.sine(t, 19, 2.4 * tc.sine(t, 1)) \
            + 0.002 * tc.sine(t, 36, 2 * tc.sine(t, 1, 5 * tc.sine(t, 1)))
        v_er = vowel_filters(v_er, sample_rate)

        v_ih = 0.22 * tc.sine(t, 1, 1.6 * tc.sine(t, 1)) \
            + 0.033 * tc.sine(t, 18, 5 * tc.sine(t, 1)) \
            + 0.005 * tc.sine(t, 30, 1.7 * tc.sine(t, 1)) \
            + 0.003 * tc.sine(t, 35, 4 * tc.sine(t, 1, 7 * tc.sine(t, 1)))
        v_ih = vowel_filters(v_ih, sample_rate)

        v_iy = 0.27 * tc.sine(t, 1, 1.6 * tc.sine(t, 1)) \
            + 0.03 * tc.sine(t, 19, 4.5 * tc.sine(t, 1)) \
            + 0.007 * tc.sine(t, 32, 1.7 * tc.sine(t, 1)) \
            + 0.003 * tc.sine(t, 35, 4 * tc.sine(t, 1, 7 * tc.sine(t, 1)))
        v_iy = vowel_filters(v_iy, sample_rate)

        v_uh = 0.28 * tc.sine(t, 2, 3.6 * tc.sine(t, 1)) \
            + 0.003 * tc.sine(t, 14, 1.6 * tc.sine(t, 1)) \
            + 0.002 * tc.sine(t, 22, 2.4 * tc.sine(t, 1)) \
            + 0.001 * tc.sine(t, 32, 3 * tc.sine(t, 1, 6 * tc.sine(t, 1)))
        v_uh = vowel_filters(v_uh, sample_rate)

        v_uw = 0.36 * tc.sine(t, 1, 2.4 * tc.sine(t, 1)) \
            + 0.008 * tc.sine(t, 16, 2 * tc.sine(t, 1)) \
            + 0.002 * tc.sine(t, 20, 2.4 * tc.sine(t, 1)) \
            + 0.0001 * tc.sine(t, 28, 3 * tc.sine(t, 1, 4 * tc.sine(t, 1)))
        v_uw = vowel_filters(v_uw, sample_rate)

        v_r = 0.3 * tc.sine(t, 2, 1.4 * tc.sine(t, 1)) \
            + 0.04 * tc.sine(t, 8, 2.3 * tc.sine(t, 1)) \
            + 0.01 * tc.sine(t, 16, 3 * tc.sine(t, 1)) \
            + 0.0012 * tc.sine(t, 34, 3 * tc.sine(t, 1, 2.5 * tc.sine(t, 1)))
        v_r = vowel_filters(v_r, sample_rate)

        v_m = 0.3 * tc.sine(t, 2, 4 * tc.sine(t, 1)) \
            + 0.02 * tc.sine(t, 10, 4 * tc.sine(t, 1))
        v_m = vowel_filters(v_m, sample_rate)

        v_n = 0.3 * tc.sine(t, 3, 5 * tc.sine(t, 1)) \
            + 0.03 * tc.sine(t, 12, 4 * tc.sine(t, 1))
        v_n = vowel_filters(v_n, sample_rate)

        v_ng = 0.33 * tc.sine(t, 3, 3 * tc.sine(t, 1)) \
            + 0.01 * tc.sine(t, 9, 4 * tc.sine(t, 1))
        v_ng = vowel_filters(v_ng, sample_rate)

        v_l = 0.3 * tc.sine(t, 1, 4 * tc.sine(t, 1)) \
            + 0.03 * tc.sine(t, 8, 3 * tc.sine(t, 1)) \
            + 0.01 * tc.sine(t, 15, 3 * tc.sine(t, 1))
        v_l = vowel_filters(v_l, sample_rate)

    oto_vowels = lambda al: [_oto % al for _oto in [
        OtoEntry('- %s', 0.0, 0.0, 900.0, 25.0, 10.0),
        OtoEntry('%s', 0.0, 300.0, 200.0, 25.0, 100.0),
        OtoEntry('%s -', 900.0, 99.0, 0.1, 60.0, 100.0)
    ]]

    if not skip_vowels:
        tc.save_sep(v_aa * vowel_env, 'aa', oto_vowels('aa'))
        tc.save_sep(v_ae * vowel_env, 'ae', oto_vowels('ae'))
        tc.save_sep(v_ae * vowel_env, 'ai', oto_vowels('ai')) # OpenUTaU C+V contains a weird 'ai' phoneme, as 'a' in 'carry'. Doesn't seem different from 'ae'.
        tc.save_sep(v_ah * vowel_env, 'ah', oto_vowels('ah'))
        tc.save_sep(v_ao * vowel_env, 'ao', oto_vowels('ao'))
        tc.save_sep(v_ax * vowel_env, 'ax', oto_vowels('ax'))
        tc.save_sep(v_eh * vowel_env, 'eh', oto_vowels('eh'))
        tc.save_sep(v_er * vowel_env, 'er', oto_vowels('er'))
        tc.save_sep(v_ih * vowel_env, 'ih', oto_vowels('ih'))
        tc.save_sep(v_iy * vowel_env, 'iy', oto_vowels('iy'))
        tc.save_sep(v_uh * vowel_env, 'uh', oto_vowels('uh'))
        tc.save_sep(v_uw * vowel_env, 'uw', oto_vowels('uw'))

    # === Diphthongs ===

    diph_1_env = np.exp(-10 * tvar ** 2)
    diph_2_env = 0.7 * np.exp(-2 * (1.2 + np.log(tvar + 1e-10)) ** 2)
    diph_3_env = 1 - np.exp(-5 * tvar ** 2)
    diphthong = lambda w1, w2, w3: diph_1_env * w1 + diph_2_env * w2 + diph_3_env * w3

    oto_v_nasals = OtoEntry('%s', 300.0, 200.0, 200.0, 50.0, 100.0)
    oto_diphs = lambda al: [_oto % al for _oto in [
        OtoEntry('- %s', 0.0, 0.0, 900.0, 25.0, 10.0),
        OtoEntry('%s', 0.0, 500.0, 200.0, 40.0, 100.0),
        OtoEntry('%s-', 400.0, 900.0, 300.0, 80.0, 40.0),
        OtoEntry('%s -', 900.0, 99.0, 0.1, 60.0, 100.0)
    ]]

    if True:
        v_aa_r = diphthong(v_aa, v_aa, v_r)
        v_ae_n = diphthong(v_ae, v_ax, v_n)
        v_ae_ng = diphthong(v_ae, v_ax, v_ng)
        v_ao_r = diphthong(v_ao, v_ao, v_r)
        v_eh_r = diphthong(v_eh, v_er, v_r)
        v_ih_ng = diphthong(v_ih, v_ax, v_ng)
        v_ih_r = diphthong(v_ih, v_ih, v_r)
        v_aw_n = diphthong(v_aa, v_uh, v_n)
        v_aw = diphthong(v_aa, v_ao, v_uh)
        v_ay = diphthong(v_aa, v_ae, v_ih)
        v_ey = diphthong(v_eh, v_ih, v_ih)
        v_ow = diphthong(v_ax, v_ao, v_uh)
        v_oy = diphthong(v_ao, v_eh, v_ih)

    if not skip_diphthongs:
        tc.save(v_aa_r, 'aa_r', oto_v_nasals % 'aa r')
        tc.save(v_ae_n, 'ae_n', oto_v_nasals % 'ae n')
        tc.save(v_ae_ng, 'ae_ng', oto_v_nasals % 'ae ng')
        tc.save(v_ao_r, 'ao_r', oto_v_nasals % 'ao r')
        tc.save(v_eh_r, 'eh_r', oto_v_nasals % 'eh r')
        tc.save(v_ih_ng, 'ih_ng', oto_v_nasals % 'ih ng')
        tc.save(v_ih_r, 'ih_r', oto_v_nasals % 'ih r')
        tc.save(v_aw_n, 'aw_n', oto_v_nasals % 'aw n')
        tc.save_sep(v_aw, 'aw', oto_diphs('aw'))
        tc.save_sep(v_ay, 'ay', oto_diphs('ay'))
        tc.save_sep(v_ey, 'ey', oto_diphs('ey'))
        tc.save_sep(v_ow, 'ow', oto_diphs('ow'))
        tc.save_sep(v_oy, 'oy', oto_diphs('oy'))

    # === Multiplexes ===

    startpoint = 0.1 * t
    endpoint = 0.8 * t
    clip = lambda x: np.clip(x, 0, 1)
    vowel_env_plos = 1 - clip(np.exp(-18 * (tvar - 0.1075))) ** 2 - clip(np.exp(27 * (tvar - 0.8)))
    vowel_env_frict = clip(1 - np.exp(-18 * (tvar - 0.11)) - np.exp(27 * (tvar - 0.8))) * (0.51 + np.arctan(50 * (tvar - 0.13)) / np.pi)

    m_ax_plos = v_ax * vowel_env_plos
    m_ax_frict = v_ax * vowel_env_frict
    cplos = lambda c1, c2: tc.shift_add(tc.shift_add(m_ax_plos, c1, startpoint), c2, endpoint)
    cfrict = lambda c1, c2: tc.shift_add(tc.shift_add(m_ax_frict, c1, startpoint), c2, endpoint)

    white_noise_base = tc.noise(t) * 1.25
    voiced_noise_base = tc.noise(t) * 0.4 + tc.saw(t, 1) * 0.75
    plosive_env = np.exp(-(4.5 + np.log(tvar + 1e-10)) ** 2) * 1.2
    fricative_env = np.clip(1 - np.exp(-300 * tvar) - np.exp(100 * (tvar - 0.055)), 0, 1) * 0.7
    affricate_env = np.sqrt(plosive_env * fricative_env) * 0.8

    oto_plosives = lambda al: [_oto % al for _oto in [
        OtoEntry('- %s', 60.0, 45.0, 890.0, 40.0, 15.0),
        OtoEntry('%s', 800.0, 20.0, 175.0, 10.0, 15.0),
        OtoEntry('%s -', 800.0, 80.0, 100.0, 10.0, 15.0)
    ]]
    oto_plosives_lead = lambda al: [_oto % al for _oto in [
        OtoEntry('- %s', 60.0, 45.0, 890.0, 40.0, 15.0),
        OtoEntry('%s', 100.0, 15.0, 880.0, 15.0, 15.0)
    ]]
    oto_fricatives = lambda al: [_oto % al for _oto in [
        OtoEntry('- %s', 60.0, 45.0, 890.0, 40.0, 15.0),
        OtoEntry('%s', 800.0, 20.0, 175.0, 10.0, 15.0),
        OtoEntry('%s -', 800.0, 80.0, 100.0, 10.0, 15.0)
    ]]
    oto_affricates = lambda al: [_oto % al for _oto in [
        OtoEntry('- %s', 60.0, 45.0, 890.0, 40.0, 15.0),
        OtoEntry('%s', 800.0, 20.0, 175.0, 10.0, 15.0),
        OtoEntry('%s -', 800.0, 80.0, 100.0, 10.0, 15.0)
    ]]
    oto_nasal_taps = lambda al: [_oto % al for _oto in [
        OtoEntry('- %s', 60.0, 45.0, 890.0, 40.0, 15.0),
        OtoEntry('%s', 800.0, 20.0, 175.0, 10.0, 15.0),
        OtoEntry('%s -', 800.0, 80.0, 100.0, 10.0, 15.0)
    ]]
    oto_half_vowels = lambda al: [_oto % al for _oto in [
        OtoEntry('- %s', 60.0, 45.0, 890.0, 40.0, 15.0),
        OtoEntry('%s', 100.0, 15.0, 870.0, 15.0, 15.0)
    ]]

    # === Consonants ===
    # Saved in a C-ax-C matter

    c_p_filter = Pedalboard([
        Gain(-15),
        PeakFilter(1000, 15, 1000 / 500),
        HighShelfFilter(6000, -35)
    ])
    c_b = c_p_filter(voiced_noise_base, sample_rate) * plosive_env
    c_p = c_p_filter(white_noise_base, sample_rate) * plosive_env

    c_sh_filter = Pedalboard([
        Gain(-5),
        PeakFilter(3000, 12, 3000 / 1500),
        LowShelfFilter(1200, -35),
        HighShelfFilter(11000, -35)
    ])
    c_ch = c_sh_filter(white_noise_base, sample_rate) * affricate_env
    c_jh = c_sh_filter(voiced_noise_base, sample_rate) * affricate_env
    c_sh = c_sh_filter(white_noise_base, sample_rate) * fricative_env
    c_zh = c_sh_filter(voiced_noise_base, sample_rate) * fricative_env

    c_t_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1800, 18, 1800 / 1800),
        PeakFilter(5000, 8, 5000 / 3000),
        HighShelfFilter(10000, -50)
    ])
    c_d = c_t_filter(voiced_noise_base, sample_rate) * plosive_env
    c_dx = c_t_filter(voiced_noise_base, sample_rate) * affricate_env * 0.75
    c_t = c_t_filter(white_noise_base, sample_rate) * plosive_env

    c_th_filter = Pedalboard([
        Gain(-5),
        PeakFilter(6000, 10, 6000 / 2500),
        PeakFilter(2500, 4, 2500 / 1250),
        LowShelfFilter(1000, -35),
        HighShelfFilter(10000, -45)
    ])
    c_dh = c_th_filter(voiced_noise_base, sample_rate) * fricative_env
    c_th = c_th_filter(white_noise_base, sample_rate) * fricative_env

    c_f_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1600, 12, 1600 / 900),
        PeakFilter(4000, 7, 4000 / 2500),
        HighShelfFilter(7000, -50)
    ])
    c_f = c_f_filter(white_noise_base, sample_rate) * fricative_env
    c_v = c_f_filter(voiced_noise_base, sample_rate) * fricative_env

    c_k_filter = Pedalboard([
            Gain(-11),
            PeakFilter(1500, 20, 2000 / 800),
            PeakFilter(5000, 11, 5000 / 1000),
            HighShelfFilter(10000, -65)
        ])
    c_g = c_k_filter(voiced_noise_base, sample_rate) * plosive_env
    c_k = c_k_filter(white_noise_base, sample_rate) * plosive_env

    c_hh_filter = Pedalboard([
        Gain(-15),
        PeakFilter(1900, 7, 1900 / 1000),
        PeakFilter(6000, 5, 6000 / 3000),
        HighShelfFilter(8000, -50)
    ])
    c_hh = c_hh_filter(white_noise_base, sample_rate) * fricative_env

    c_l = v_l * affricate_env
    c_m = v_m * affricate_env
    c_n = v_n * affricate_env
    c_ng = v_ng * affricate_env
    c_r = v_r * affricate_env

    c_q = plosive_env * 0.0 # WTF

    c_s_filter = Pedalboard([
        Gain(-5),
        PeakFilter(7200, 13, 7200 / 4500),
        LowShelfFilter(2250, -35),
        HighShelfFilter(11250, -45)
    ])
    c_s = c_s_filter(white_noise_base, sample_rate) * affricate_env
    c_z = c_s_filter(voiced_noise_base, sample_rate) * affricate_env

    c_w = v_uw * np.exp(-9 * tvar) * vowel_env
    c_y = v_iy * np.exp(-9 * tvar) * vowel_env

    if not skip_consonants:
        tc.save_sep(cplos(c_b, c_b),    'b_ax_b',   oto_plosives('b'))
        tc.save_sep(cfrict(c_ch, c_ch), 'ch_ax_ch', oto_affricates('ch'))
        tc.save_sep(cplos(c_d, c_d),    'd_ax_d',   oto_plosives('d'))
        tc.save_sep(cfrict(c_dh, c_dh), 'dh_ax_dh', oto_fricatives('dh'))
        tc.save_sep(cplos(c_dx, None),  'dx_ax',    oto_plosives_lead('dx'))
        tc.save_sep(cfrict(c_f, c_f),   'f_ax_f',   oto_fricatives('f'))
        tc.save_sep(cplos(c_g, c_g),    'g_ax_g',   oto_plosives('g'))
        tc.save_sep(cfrict(c_hh, c_hh), 'hh_ax_hh', oto_fricatives('hh'))
        tc.save_sep(cfrict(c_jh, c_jh), 'jh_ax_jh', oto_affricates('jh'))
        tc.save_sep(cplos(c_k, c_k),    'k_ax_k',   oto_plosives('k'))
        tc.save_sep(cfrict(c_l, c_l),   'l_ax_l',   oto_nasal_taps('l'))
        tc.save_sep(cfrict(c_m, c_m),   'm_ax_m',   oto_nasal_taps('m'))
        tc.save_sep(cfrict(c_n, c_n),   'n_ax_n',   oto_nasal_taps('n'))
        tc.save_sep(cfrict(c_ng, c_ng), 'ng_ax_ng', oto_nasal_taps('ng'))
        tc.save_sep(cplos(c_p, c_p),    'p_ax_p',   oto_plosives('p'))
        tc.save_sep(cplos(c_q, c_q),    'q_ax_q',   oto_plosives('q'))
        tc.save_sep(cfrict(c_r, c_r),   'r_ax_r',   oto_nasal_taps('r'))
        tc.save_sep(cfrict(c_s, c_s),   's_ax_s',   oto_fricatives('s'))
        tc.save_sep(cfrict(c_sh, c_sh), 'sh_ax_sh', oto_fricatives('sh'))
        tc.save_sep(cplos(c_t, c_t),    't_ax_t',   oto_plosives('t'))
        tc.save_sep(cfrict(c_th, c_th), 'th_ax_th', oto_fricatives('th'))
        tc.save_sep(cfrict(c_v, c_v),   'v_ax_v',   oto_fricatives('v'))
        tc.save_sep(cfrict(c_w, None),  'w_ax',     oto_half_vowels('w'))
        tc.save_sep(cfrict(c_y, None),  'y_ax',     oto_half_vowels('y'))
        tc.save_sep(cfrict(c_z, c_z),   'z_ax_z',   oto_fricatives('z'))
        tc.save_sep(cfrict(c_zh, c_zh), 'zh_ax_zh', oto_fricatives('zh'))

    # === Extras ===

    x_br1_filter = Pedalboard([
        Gain(-14),
        PeakFilter(2000, 8, 2000 / 1000),
        PeakFilter(6000, 4, 6000 / 3000),
        HighShelfFilter(10000, -45)
    ])
    x_br1 = x_br1_filter(white_noise_base, sample_rate) * np.exp(-1000 * (tvar - 0.08) ** 2)
    oto_br1 = OtoEntry('', 20.0, 105.0, 875.0, 20.0, 5.0)

    x_br2_filter = Pedalboard([
        Gain(-14),
        PeakFilter(1900, 8, 1900 / 1000),
        PeakFilter(5800, 4, 5800 / 3000),
        HighShelfFilter(9200, -47)
    ])
    x_br2 = x_br2_filter(white_noise_base, sample_rate) * np.exp(-300 * (tvar - 0.15) ** 2)
    oto_br2 = OtoEntry('', 40.0, 200.0, 760.0, 20.0, 5.0)

    x_br3_filter = Pedalboard([
        Gain(-13),
        PeakFilter(1800, 8, 1800 / 1000),
        PeakFilter(5500, 4, 5500 / 3000),
        HighShelfFilter(8700, -49)
    ])
    x_br3 = x_br3_filter(white_noise_base, sample_rate) * np.exp(-190 * (tvar - 0.19) ** 2)
    oto_br3 = OtoEntry('', 60.0, 250.0, 690.0, 20.0, 5.0)

    if not skip_extras:
        tc.save(x_br1, 'br1', oto_br1)
        tc.save(x_br2, 'br2', oto_br2)
        tc.save(x_br3, 'br3', oto_br3)

    tc.save_oto()

    config = {
        'text_file_encoding': 'utf-8',
        'name': 'Technebit β1.0 En-C+V',
        'localized_names': {
            'ja-JP': 'テクネビット β1.0 英語-C+V',
            'zh-CN': '锝比特 β1.0 英语-C+V',
            'zh-TW': '鍀比特 β1.0 英語-C+V'
        },
        'author': 'Generated soundbank - Python program by Nomani',
        'voice': 'FM Synthesizer (literally)',
        'version': 'β1.0',
        'web': 'https://github.com/Nomani-int64/Technebit',
        'default_phonemizer': 'OpenUtau.Plugin.Builtin.EnglishCpVPhonemizerBETA',
        'image': {
            'base': 'image_beta_en_c+v_b1.0.png',
            'overlay': {
                'text': 'Tcb En-C+V\nb1.0',
                'color': (0, 192, 127),
                'pos': 'bottom_right',
                'size': 20
            }
        },
        'portrait': {
            'base': 'portrait_beta.png',
            'opacity': 0.6,
            'height': 0,
            'overlay': {
                'text': 'Technebit En-C+V b1.0\nGen time {t}\n{s}',
                'color': (64, 64, 64),
                'pos': 'bottom_right',
                'size': 24
            }
        },
        'extra': 'This voicebank is generated by Python code, see web for Github repo.\n'
                 'Please label with original author when you use and redistribute the program and generated voicebank.\n'
                 '~~~ About Technebit the character ~~~\n'
                 'Technebit is a robot with super computility and AI-based consciousness.\n'
                 'Its base part is a 80 cm cube, and weighs ~64 kg.\n'
                 'Technebit likes all kinds of playful interactions with users, and sees this as its meaning of existence.'
    }
    tc.make_info(config)

    print(f'[Info] All files finished, time span {time.time() - start_time}s.')
    tc.alarm()

if __name__ == '__main__':
    generate()
