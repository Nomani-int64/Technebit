from tc_utils import *

def generate():
    '''
    Generates the entire UTaU Japanese CV soundbank. Should and only be called once.

    The syllable names mainly refers to Hebon-shiki Romaji(ヘボン式ローマ字), with some features listed below:
    - Consonants followed with a single -y means it will connect with i or y-(e.g. きゃ=ky+ya);
    - を is pronounced as 'wo' here;
    - Some kanas are tweaked to match actual sounds(e.g. ち=chi, つ=tsu, てぃ=ti, とぅ=tu);
    - Some kanas in Da-gyo(だ行) are omitted, for they actually share pronunciation with other kanas(e.g. ぢ==じ, づ==ず);
    - ふ does not concatenate with w- sounds, unlike most others(e.g. くぁ=kwa, but ふぁ=fa);
    - Nasal-voiced ga-gyo sounds are notated as ng-(e.g. か゜=nga) and aliased with katakanas.

    The variable prefixes are as follows:
    - v_ variables are standalone vowels and nasals;
    - c_ variables are standalone consonants;
    - m_ variables are connecting vowels. In addition, ms_ connects better to plosive consonants, and mf_ to frictive consonants;
    - s_ variables are complete syllables and are ready to export;
    - x_ variables are for extra sounds;
    - oto_ variables are, obviously, oto entries.
    '''

    start_time = time.time()

    t = 1.0
    base_freq = 220.0
    sample_rate = 44100

    tc = Tc(sample_rate, base_freq, '\0Tcb b1.0 Ja-CV', False)
    tvar = np.linspace(0.0, t, int(t * sample_rate), False)

    # Skip flags
    # Useful for debugging and modifying, set to True to SKIP EXPORTS
    #   (calculations are never skipped as multiplexing exists)

    skip_a_gyo = False
    skip_ya_gyo = False
    skip_wa_gyo = False
    skip_ka_gyo = False
    skip_ga_gyo = False
    skip_sa_gyo = False
    skip_za_gyo = False
    skip_ta_gyo = False
    skip_da_gyo = False
    skip_na_gyo = False
    skip_ha_gyo = False
    skip_pa_gyo = False
    skip_ba_gyo = False
    skip_ma_gyo = False
    skip_ra_gyo = False
    skip_extras = False

    # === Vowels / A-gyo ===
    # Contains あいうえお and nasals ん(m/n/ng); heavily multiplexed

    vowel_env = (1 - np.exp(-27 * tvar) - np.exp(27 * (tvar - t))) * (0.75 + np.exp(-15 * tvar))
    vowel_filters = Pedalboard([
        PeakFilter(220, -20, 220 / 40),
        PeakFilter(660, -15, 660 / 30),
        PeakFilter(1500, -7.5, 660 / 720),
        Gain(5)
    ])

    v_a = 0.3 * tc.sine(t, 5, 2 * tc.sine(t, 1)) \
        + 0.02 * tc.sine(t, 15, 8 * tc.sine(t, 1)) \
        + 0.01 * tc.sine(t, 21, 3 * tc.sine(t, 1)) \
        + 0.004 * tc.sine(t, 26, 4 * tc.sine(t, 1, 8 * tc.sine(t, 1)))
    v_a = vowel_filters(v_a, sample_rate)

    v_i = 0.27 * tc.sine(t, 1, 1.6 * tc.sine(t, 1)) \
        + 0.03 * tc.sine(t, 19, 4.5 * tc.sine(t, 1)) \
        + 0.007 * tc.sine(t, 32, 1.7 * tc.sine(t, 1)) \
        + 0.003 * tc.sine(t, 35, 4 * tc.sine(t, 1, 7 * tc.sine(t, 1)))
    v_i = vowel_filters(v_i, sample_rate)

    v_u = 0.28 * tc.sine(t, 2, 3.6 * tc.sine(t, 1)) \
        + 0.0075 * tc.sine(t, 15, 1.6 * tc.sine(t, 1)) \
        + 0.008 * tc.sine(t, 22, 2.4 * tc.sine(t, 1)) \
        + 0.005 * tc.sine(t, 32, 3 * tc.sine(t, 1, 6 * tc.sine(t, 1)))
    v_u = vowel_filters(v_u, sample_rate)

    v_e = 0.2 * tc.sine(t, 2, 2.5 * tc.sine(t, 1)) \
        + 0.06 * tc.sine(t, 16, 4.5 * tc.sine(t, 1)) \
        + 0.006 * tc.sine(t, 32, 1.7 * tc.sine(t, 1)) \
        + 0.0025 * tc.sine(t, 45, 4 * tc.sine(t, 1, 4 * tc.sine(t, 1)))
    v_e = vowel_filters(v_e, sample_rate)

    v_o = 0.3 * tc.sine(t, 2, 3 * tc.sine(t, 1)) \
        + 0.07 * tc.sine(t, 2, 5 * tc.sine(t, 1)) \
        + 0.015 * tc.sine(t, 21, 1.8 * tc.sine(t, 1)) \
        + 0.002 * tc.sine(t, 24, 4 * tc.sine(t, 1, 8 * tc.sine(t, 1)))
    v_o = vowel_filters(v_o, sample_rate)

    v_m = 0.3 * tc.sine(t, 2, 4 * tc.sine(t, 1)) \
        + 0.02 * tc.sine(t, 10, 4 * tc.sine(t, 1))
    v_m = vowel_filters(v_m, sample_rate)

    v_n = 0.3 * tc.sine(t, 3, 5 * tc.sine(t, 1)) \
        + 0.03 * tc.sine(t, 12, 4 * tc.sine(t, 1))
    v_n = vowel_filters(v_n, sample_rate)

    v_ng = 0.33 * tc.sine(t, 3, 3 * tc.sine(t, 1)) \
        + 0.01 * tc.sine(t, 9, 4 * tc.sine(t, 1))
    v_ng = vowel_filters(v_ng, sample_rate)

    v_r = 0.27 * tc.sine(t, 5, 5 * tc.sine(t, 1)) \
        + 0.01 * tc.sine(t, 10, 4 * tc.sine(t, 1))
    v_r = vowel_filters(v_r, sample_rate)

    oto_vowels = OtoEntry('_', 0.0, 300.0, 200.0, 25.0, 10.0)

    if not skip_a_gyo:
        tc.save(v_a * vowel_env, 'a', oto_vowels.as_name('あ'), True)
        tc.save(v_i * vowel_env, 'i', oto_vowels.as_name('い'), True)
        tc.save(v_u * vowel_env, 'u', oto_vowels.as_name('う'), True)
        tc.save(v_e * vowel_env, 'e', oto_vowels.as_name('え'), True)
        tc.save(v_o * vowel_env, 'o', oto_vowels.as_name('お'), True)
        tc.save(v_m * vowel_env, 'm', oto_vowels.as_name('んm'), True)
        tc.save(v_n * vowel_env, 'n', oto_vowels.as_name('ん'), True)
        tc.save(v_ng * vowel_env, 'ng', oto_vowels.as_name('んg'), True)

    # === Semivowels / Ya-gyo & wa-gyo ===
    # Contains やゆいぇよ　わうぃうぇを; multiplexed

    s_ya = (v_i * np.exp(-9 * tvar) + v_a * (1 - np.exp(-18 * tvar)))
    s_yu = (v_i * np.exp(-9 * tvar) + v_u * (1 - np.exp(-18 * tvar)))
    s_ye = (v_i * np.exp(-9 * tvar) + v_e * (1 - np.exp(-18 * tvar)))
    s_yo = (v_i * np.exp(-9 * tvar) + v_o * (1 - np.exp(-18 * tvar)))
    s_wa = (v_u * np.exp(-9 * tvar) + v_a * (1 - np.exp(-18 * tvar)))
    s_wi = (v_u * np.exp(-9 * tvar) + v_i * (1 - np.exp(-18 * tvar)))
    s_we = (v_u * np.exp(-9 * tvar) + v_e * (1 - np.exp(-18 * tvar)))
    s_wo = (v_u * np.exp(-9 * tvar) + v_o * (1 - np.exp(-18 * tvar)))

    oto_semivowels = OtoEntry('_', 0.0, 300.0, 200.0, 30.0, 10.0)

    if not skip_ya_gyo:
        tc.save(s_ya * vowel_env, 'ya', oto_semivowels.as_name('や'), True)
        tc.save(s_yu * vowel_env, 'yu', oto_semivowels.as_name('ゆ'), True)
        tc.save(s_ye * vowel_env, 'ye', oto_semivowels.as_name('いぇ'), True)
        tc.save(s_yo * vowel_env, 'yo', oto_semivowels.as_name('よ'), True)
    if not skip_wa_gyo:
        tc.save(s_wa * vowel_env, 'wa', oto_semivowels.as_name('わ'), True)
        tc.save(s_wi * vowel_env, 'wi', oto_semivowels.as_name('うぃ'), True)
        tc.save(s_we * vowel_env, 'we', oto_semivowels.as_name('うぇ'), True)
        tc.save(s_wo * vowel_env, 'wo', oto_semivowels.as_name('を'), True)

    # === Multiplexes ===
    # Multiplexing for similar structures in all kinds of syllables and also oto entries

    vowel_env_plos = 1 - np.clip(np.exp(-18 * (tvar - 0.01)), 0, 1) ** 2 - np.exp(27 * (tvar - t))
    vowel_env_frict = (1 - np.exp(-18 * (tvar - 0.01)) - np.exp(27 * (tvar - t))) * (0.5 + np.arctan(50 * (tvar - 0.03)) / np.pi)
    semivowel_env_concat = 1 - np.clip(np.exp(-27 * (tvar - 0.01)), 0, 1) - np.exp(27 * (tvar - t))

    ms_a = v_a * vowel_env_plos
    ms_i = v_i * vowel_env_plos
    ms_u = v_u * vowel_env_plos
    ms_e = v_e * vowel_env_plos
    ms_o = v_o * vowel_env_plos
    mf_a = v_a * vowel_env_frict
    mf_i = v_i * vowel_env_frict
    mf_u = v_u * vowel_env_frict
    mf_e = v_e * vowel_env_frict
    mf_o = v_o * vowel_env_frict
    m_ya = tc.shift_add(tvar * 0, s_ya, 0.01) * semivowel_env_concat
    m_yu = tc.shift_add(tvar * 0, s_yu, 0.01) * semivowel_env_concat
    m_ye = tc.shift_add(tvar * 0, s_ye, 0.01) * semivowel_env_concat
    m_yo = tc.shift_add(tvar * 0, s_yo, 0.01) * semivowel_env_concat
    m_wa = tc.shift_add(tvar * 0, s_wa, 0.01) * semivowel_env_concat
    m_wi = tc.shift_add(tvar * 0, s_wi, 0.01) * semivowel_env_concat
    m_we = tc.shift_add(tvar * 0, s_we, 0.01) * semivowel_env_concat
    m_wo = tc.shift_add(tvar * 0, s_wo, 0.01) * semivowel_env_concat

    white_noise_base = tc.noise(t)
    voiced_noise_base = tc.noise(t) * 0.2 + tc.saw(t, 1) * 0.6
    plosive_env = np.exp(-(4.5 + np.log(tvar + 1e-10)) ** 2) * 1.2
    fricative_env = np.clip(1 - np.exp(-300 * tvar) - np.exp(100 * (tvar - 0.055)), 0, 1)
    affricate_env = np.sqrt(plosive_env * fricative_env) * 0.8

    oto_plosives = OtoEntry('_', 4.0, 300.0, 200.0, 30.0, 5.0)
    oto_fricatives = OtoEntry('_', 0.0, 300.0, 200.0, 30.0, 15.0)
    oto_affricates = OtoEntry('_', 4.0, 300.0, 200.0, 30.0, 5.0)
    oto_nasal_taps = OtoEntry('_', 0.0, 300.0, 200.0, 30.0, 15.0)
    oto_plosives_alone = OtoEntry('', 4.0, 120.0, 880.0, 15.0, 5.0)
    oto_fricatives_alone = OtoEntry('', 0.0, 30.0, 950.0, 15.0, 10.0)
    oto_affricates_alone = OtoEntry('', 4.0, 55.0, 945.0, 15.0, 5.0)
    oto_nasal_taps_alone = OtoEntry('', 0.0, 50.0, 950.0, 15.0, 10.0)

    # === Ka-gyo ===
    # Contains かきくけこ　きゃきゅきぇきょ　くぁくぃくぇくぉ

    c_k_filter = Pedalboard([
        Gain(-11),
        PeakFilter(1500, 20, 2000 / 800),
        PeakFilter(5000, 11, 5000 / 1000),
        HighShelfFilter(10000, -65)
    ])
    c_k = c_k_filter(white_noise_base, sample_rate) * plosive_env

    c_ky_filter = Pedalboard([
        Gain(-11),
        PeakFilter(2000, 18, 2000 / 900),
        PeakFilter(6000, 9, 6000 / 1000),
        HighShelfFilter(11000, -70)
    ])
    c_ky = c_ky_filter(white_noise_base, sample_rate) * plosive_env

    s_ka = c_k + ms_a;    s_ki = c_ky + ms_i;   s_ku = c_k + ms_u;    s_ke = c_k + ms_e;    s_ko = c_k + ms_o
    s_kya = c_ky + m_ya;                      s_kyu = c_ky + m_yu; s_kye = c_ky + m_ye; s_kyo = c_ky + m_yo
    s_kwa = c_k + m_wa;  s_kwi = c_k + m_wi;                       s_kwe = c_k + m_we;  s_kwo = c_k + m_wo
    if not skip_ka_gyo:
        tc.save(c_k, 'k', oto_plosives_alone.as_name(''))
        tc.save(c_ky, 'ky', oto_plosives_alone.as_name(''))
        tc.save(s_ka, 'ka', oto_plosives.as_name('か'), True)
        tc.save(s_ki, 'ki', oto_plosives.as_name('き'), True)
        tc.save(s_ku, 'ku', oto_plosives.as_name('く'), True)
        tc.save(s_ke, 'ke', oto_plosives.as_name('け'), True)
        tc.save(s_ko, 'ko', oto_plosives.as_name('こ'), True)
        tc.save(s_kya, 'kya', oto_plosives.as_name('きゃ'), True)
        tc.save(s_kyu, 'kyu', oto_plosives.as_name('きゅ'), True)
        tc.save(s_kye, 'kye', oto_plosives.as_name('きぇ'), True)
        tc.save(s_kyo, 'kyo', oto_plosives.as_name('きょ'), True)
        tc.save(s_kwa, 'kwa', oto_plosives.as_name('くぁ'), True)
        tc.save(s_kwi, 'kwi', oto_plosives.as_name('くぃ'), True)
        tc.save(s_kwe, 'kwe', oto_plosives.as_name('くぇ'), True)
        tc.save(s_kwo, 'kwo', oto_plosives.as_name('くぉ'), True)

    # === Ga-gyo ===
    # Contains がぎぐげご　ぎゃぎゅぎぇぎょ　ぐぁぐぃぐぇぐぉ

    c_g = c_k_filter(voiced_noise_base, sample_rate) * plosive_env # Convenient!?
    c_gy = c_ky_filter(voiced_noise_base, sample_rate) * plosive_env

    s_ga = c_g + ms_a;    s_gi = c_gy + ms_i;   s_gu = c_g + ms_u;    s_ge = c_g + ms_e;    s_go = c_g + ms_o
    s_gya = c_gy + m_ya;                      s_gyu = c_gy + m_yu; s_gye = c_gy + m_ye; s_gyo = c_gy + m_yo
    s_gwa = c_g + m_wa;  s_gwi = c_g + m_wi;                       s_gwe = c_g + m_we;  s_gwo = c_g + m_wo
    if not skip_ga_gyo:
        tc.save(c_g, 'g', oto_plosives_alone.as_name(''))
        tc.save(c_gy, 'gy', oto_plosives_alone.as_name(''))
        tc.save(s_ga, 'ga', oto_plosives.as_name('が'), True)
        tc.save(s_gi, 'gi', oto_plosives.as_name('ぎ'), True)
        tc.save(s_gu, 'gu', oto_plosives.as_name('ぐ'), True)
        tc.save(s_ge, 'ge', oto_plosives.as_name('げ'), True)
        tc.save(s_go, 'go', oto_plosives.as_name('ご'), True)
        tc.save(s_gya, 'gya', oto_plosives.as_name('ぎゃ'), True)
        tc.save(s_gyu, 'gyu', oto_plosives.as_name('ぎゅ'), True)
        tc.save(s_gye, 'gye', oto_plosives.as_name('ぎぇ'), True)
        tc.save(s_gyo, 'gyo', oto_plosives.as_name('ぎょ'), True)
        tc.save(s_gwa, 'gwa', oto_plosives.as_name('ぐぁ'), True)
        tc.save(s_gwi, 'gwi', oto_plosives.as_name('ぐぃ'), True)
        tc.save(s_gwe, 'gwe', oto_plosives.as_name('ぐぇ'), True)
        tc.save(s_gwo, 'gwo', oto_plosives.as_name('ぐぉ'), True)

    # === Sa-gyo ===
    # Contains さしすせそ　しゃしゅしぇしょ　すぁすぃすぇすぉ

    c_s_filter = Pedalboard([
        Gain(-5),
        PeakFilter(7200, 12, 7200 / 4500),
        LowShelfFilter(2250, -35),
        HighShelfFilter(11250, -45)
    ])
    c_s = c_s_filter(white_noise_base, sample_rate) * fricative_env

    c_sh_filter = Pedalboard([
        Gain(-5),
        PeakFilter(8000, 12, 8000 / 1500),
        LowShelfFilter(2500, -35),
        HighShelfFilter(11500, -40)
    ])
    c_sh = c_sh_filter(white_noise_base, sample_rate) * fricative_env

    s_sa = c_s + mf_a;   s_shi = c_sh + mf_i; s_su = c_s + mf_u;   s_se = c_s + mf_e;   s_so = c_s + mf_o
    s_sha = c_sh + m_ya;                      s_shu = c_sh + m_yu; s_she = c_sh + m_ye; s_sho = c_sh + m_yo
    s_swa = c_s + m_wa;  s_swi = c_s + m_wi;                       s_swe = c_s + m_we;  s_swo = c_s + m_wo
    if not skip_sa_gyo:
        tc.save(c_s, 's', oto_fricatives_alone.as_name(''))
        tc.save(c_sh, 'sh', oto_fricatives_alone.as_name(''))
        tc.save(s_sa, 'sa', oto_fricatives.as_name('さ'), True)
        tc.save(s_shi, 'shi', oto_fricatives.as_name('し'), True)
        tc.save(s_su, 'su', oto_fricatives.as_name('す'), True)
        tc.save(s_se, 'se', oto_fricatives.as_name('せ'), True)
        tc.save(s_so, 'so', oto_fricatives.as_name('そ'), True)
        tc.save(s_sha, 'sha', oto_fricatives.as_name('しゃ'), True)
        tc.save(s_shu, 'shu', oto_fricatives.as_name('しゅ'), True)
        tc.save(s_she, 'she', oto_fricatives.as_name('しぇ'), True)
        tc.save(s_sho, 'sho', oto_fricatives.as_name('しょ'), True)
        tc.save(s_swa, 'swa', oto_fricatives.as_name('すぁ'), True)
        tc.save(s_swi, 'swi', oto_fricatives.as_name('すぃ'), True)
        tc.save(s_swe, 'swe', oto_fricatives.as_name('すぇ'), True)
        tc.save(s_swo, 'swo', oto_fricatives.as_name('すぉ'), True)

    # === Za-gyo ===
    # Contains ざじずぜぞ　じゃじゅじぇじょ　ずぁずぃずぇずぉ

    c_z = c_s_filter(voiced_noise_base, sample_rate) * fricative_env
    c_j = c_sh_filter(voiced_noise_base, sample_rate) * fricative_env

    s_za = c_z + mf_a;  s_ji = c_j + mf_i;  s_zu = c_z + mf_u;  s_ze = c_z + mf_e;  s_zo = c_z + mf_o
    s_ja = c_j + m_ya;                      s_ju = c_j + m_yu;  s_je = c_j + m_ye;  s_jo = c_j + m_yo
    s_zwa = c_z + m_wa; s_zwi = c_z + m_wi;                     s_zwe = c_z + m_we; s_zwo = c_z + m_wo

    if not skip_za_gyo:
        tc.save(c_z, 'z', oto_fricatives_alone.as_name(''))
        tc.save(c_j, 'j', oto_fricatives_alone.as_name(''))
        tc.save(s_za, 'za', oto_fricatives.as_name('ざ'), True)
        tc.save(s_ji, 'ji', oto_fricatives.as_name('じ'), True)
        tc.save(s_zu, 'zu', oto_fricatives.as_name('ず'), True)
        tc.save(s_ze, 'ze', oto_fricatives.as_name('ぜ'), True)
        tc.save(s_zo, 'zo', oto_fricatives.as_name('ぞ'), True)
        tc.save(s_ja, 'ja', oto_fricatives.as_name('じゃ'), True)
        tc.save(s_ju, 'ju', oto_fricatives.as_name('じゅ'), True)
        tc.save(s_je, 'je', oto_fricatives.as_name('じぇ'), True)
        tc.save(s_jo, 'jo', oto_fricatives.as_name('じょ'), True)
        tc.save(s_zwa, 'zwa', oto_fricatives.as_name('ずぁ'), True)
        tc.save(s_zwi, 'zwi', oto_fricatives.as_name('ずぃ'), True)
        tc.save(s_zwe, 'zwe', oto_fricatives.as_name('ずぇ'), True)
        tc.save(s_zwo, 'zwo', oto_fricatives.as_name('ずぉ'), True)

    # === Ta-gyo ===
    # Contains たてぃとぅてと　ちゃちちゅちぇちょ　つぁつぃつつぇつぉ

    c_t_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1800, 18, 1800 / 1800),
        PeakFilter(5000, 8, 5000 / 3000),
        HighShelfFilter(10000, -50)
    ])
    c_t = c_t_filter(white_noise_base, sample_rate) * plosive_env

    c_ty_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1800, 18, 1800 / 1600),
        PeakFilter(5600, 8, 5600 / 3200),
        HighShelfFilter(12000, -50)
    ])
    c_ty = c_ty_filter(white_noise_base, sample_rate) * plosive_env

    c_ch_filter = Pedalboard([
        Gain(-15),
        PeakFilter(5500, 20, 5500 / 2000),
        PeakFilter(8000, 9, 8000 / 3200),
        LowShelfFilter(2000, -22),
        HighShelfFilter(12000, -15),
    ])
    c_ch = c_ch_filter(white_noise_base, sample_rate) * affricate_env

    c_ts_filter = Pedalboard([
        Gain(-10),
        PeakFilter(8000, 11, 8000 / 4000),
        PeakFilter(4000, 7, 4000 / 2000),
        HighShelfFilter(12500, -45)
    ])
    c_ts = c_ts_filter(white_noise_base, sample_rate) * affricate_env

    s_ta = c_t + ms_a;   s_ti = c_ty + ms_i;  s_tu = c_t + ms_u;   s_te = c_t + ms_e;   s_to = c_t + ms_o
    s_cha = c_ch + m_ya; s_chi = c_ch + ms_i; s_chu = c_ch + m_yu; s_che = c_ch + m_ye; s_cho = c_ch + m_yo
    s_tsa = c_ts + m_wa; s_tsi = c_ts + m_wi; s_tsu = c_ts + ms_u; s_tse = c_ts + m_we; s_tso = c_ts + m_wo
    if not skip_ta_gyo:
        tc.save(c_t, 't', oto_plosives_alone.as_name(''))
        tc.save(c_ty, 'ty', oto_plosives_alone.as_name(''))
        tc.save(c_ch, 'ch', oto_affricates_alone.as_name(''))
        tc.save(c_ts, 'ts', oto_affricates_alone.as_name(''))
        tc.save(s_ta, 'ta', oto_plosives.as_name('た'), True)
        tc.save(s_ti, 'ti', oto_plosives.as_name('てぃ'), True)
        tc.save(s_tu, 'tu', oto_plosives.as_name('とぅ'), True)
        tc.save(s_te, 'te', oto_plosives.as_name('て'), True)
        tc.save(s_to, 'to', oto_plosives.as_name('と'), True)
        tc.save(s_cha, 'cha', oto_affricates.as_name('ちゃ'), True)
        tc.save(s_chi, 'chi', oto_affricates.as_name('ち'), True)
        tc.save(s_chu, 'chu', oto_affricates.as_name('ちゅ'), True)
        tc.save(s_che, 'che', oto_affricates.as_name('ちぇ'), True)
        tc.save(s_cho, 'cho', oto_affricates.as_name('ちょ'), True)
        tc.save(s_tsa, 'tsa', oto_affricates.as_name('つぁ'), True)
        tc.save(s_tsi, 'tsi', oto_affricates.as_name('つぃ'), True)
        tc.save(s_tsu, 'tsu', oto_affricates.as_name('つ'), True)
        tc.save(s_tse, 'tse', oto_affricates.as_name('つぇ'), True)
        tc.save(s_tso, 'tso', oto_affricates.as_name('つぉ'), True)

    # === Da-gyo ===
    # Contains だでぃどぅでど; repeating pronunciations omitted

    c_d = c_t_filter(voiced_noise_base, sample_rate) * plosive_env
    c_dy = c_ty_filter(voiced_noise_base, sample_rate) * plosive_env

    s_da = c_d + ms_a; s_di = c_dy + ms_i; s_du = c_d + ms_u; s_de = c_d + ms_e; s_do = c_d + ms_o
    if not skip_da_gyo:
        tc.save(c_d, 'd', oto_plosives_alone.as_name(''))
        tc.save(c_dy, 'dy', oto_plosives_alone.as_name(''))
        tc.save(s_da, 'da', oto_plosives.as_name('だ'), True)
        tc.save(s_di, 'di', oto_plosives.as_name('でぃ'), True)
        tc.save(s_du, 'du', oto_plosives.as_name('どぅ'), True)
        tc.save(s_de, 'de', oto_plosives.as_name('で'), True)
        tc.save(s_do, 'do', oto_plosives.as_name('ど'), True)

    # === Na-gyo ===
    # Contains なにぬねの　にゃにゅにぇにょ　ぬぁぬぃぬぇぬぉ

    c_n = v_n * affricate_env

    s_na = c_n + ms_a;  s_ni = c_n + ms_i;  s_nu = c_n + ms_u;  s_ne = c_n + ms_e;  s_no = c_n + ms_o
    s_nya = c_n + m_ya;                     s_nyu = c_n + m_yu; s_nye = c_n + m_ye; s_nyo = c_n + m_yo
    s_nwa = c_n + m_wa; s_nwi = c_n + m_wi;                     s_nwe = c_n + m_we; s_nwo = c_n + m_wo
    if not skip_na_gyo:
        tc.save(c_n, 'n_', oto_nasal_taps_alone.as_name(''))
        tc.save(s_na, 'na', oto_nasal_taps.as_name('な'), True)
        tc.save(s_ni, 'ni', oto_nasal_taps.as_name('に'), True)
        tc.save(s_nu, 'nu', oto_nasal_taps.as_name('ぬ'), True)
        tc.save(s_ne, 'ne', oto_nasal_taps.as_name('ね'), True)
        tc.save(s_no, 'no', oto_nasal_taps.as_name('の'), True)
        tc.save(s_nya, 'nya', oto_nasal_taps.as_name('にゃ'), True)
        tc.save(s_nyu, 'nyu', oto_nasal_taps.as_name('にゅ'), True)
        tc.save(s_nye, 'nye', oto_nasal_taps.as_name('にぇ'), True)
        tc.save(s_nyo, 'nyo', oto_nasal_taps.as_name('にょ'), True)
        tc.save(s_nwa, 'nwa', oto_nasal_taps.as_name('ぬぁ'), True)
        tc.save(s_nwi, 'nwi', oto_nasal_taps.as_name('ぬぃ'), True)
        tc.save(s_nwe, 'nwe', oto_nasal_taps.as_name('ぬぇ'), True)
        tc.save(s_nwo, 'nwo', oto_nasal_taps.as_name('ぬぉ'), True)

    # === Ha-gyo ===
    # Contains はひほぅへほ　ひゃひゅひぇひょ　ふぁふぃふふぇふぉ

    c_h_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1700, 10, 1700 / 1000),
        PeakFilter(5500, 5, 5500 / 3000),
        HighShelfFilter(8000, -50)
    ])
    c_h = c_h_filter(white_noise_base, sample_rate) * fricative_env

    c_hy_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1500, 10, 1500 / 900),
        PeakFilter(6500, 5, 6500 / 3200),
        HighShelfFilter(8800, -52)
    ])
    c_hy = c_hy_filter(white_noise_base, sample_rate) * fricative_env

    c_f_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1400, 9, 1400 / 900),
        PeakFilter(4000, 6, 4000 / 2500),
        HighShelfFilter(7000, -50)
    ])
    c_f = c_f_filter(white_noise_base, sample_rate) * fricative_env

    s_ha = c_h + mf_a;   s_hi = c_hy + mf_i; s_hu = c_h + mf_u;   s_he = c_h + mf_e;   s_ho = c_h + mf_o
    s_hya = c_hy + m_ya;                     s_hyu = c_hy + m_yu; s_hye = c_hy + m_ye; s_hyo = c_hy + m_yo
    s_fa = c_f + mf_a;   s_fi = c_f + mf_i;  s_fu = c_f + mf_u;   s_fe = c_f + mf_e;   s_fo = c_f + mf_o
    if not skip_ha_gyo:
        tc.save(c_h, 'h', oto_fricatives_alone.as_name(''))
        tc.save(c_hy, 'hy', oto_fricatives_alone.as_name(''))
        tc.save(c_f, 'f', oto_fricatives_alone.as_name(''))
        tc.save(s_ha, 'ha', oto_fricatives.as_name('は'), True)
        tc.save(s_hi, 'hi', oto_fricatives.as_name('ひ'), True)
        tc.save(s_hu, 'hu', oto_fricatives.as_name('ほぅ'), True)
        tc.save(s_he, 'he', oto_fricatives.as_name('へ'), True)
        tc.save(s_ho, 'ho', oto_fricatives.as_name('ほ'), True)
        tc.save(s_hya, 'hya', oto_fricatives.as_name('ひゃ'), True)
        tc.save(s_hyu, 'hyu', oto_fricatives.as_name('ひゅ'), True)
        tc.save(s_hye, 'hye', oto_fricatives.as_name('ひぇ'), True)
        tc.save(s_hyo, 'hyo', oto_fricatives.as_name('ひょ'), True)
        tc.save(s_fa, 'fa', oto_fricatives.as_name('ふぁ'), True)
        tc.save(s_fi, 'fi', oto_fricatives.as_name('ふぃ'), True)
        tc.save(s_fu, 'fu', oto_fricatives.as_name('ふ'), True)
        tc.save(s_fe, 'fe', oto_fricatives.as_name('ふぇ'), True)
        tc.save(s_fo, 'fo', oto_fricatives.as_name('ふぉ'), True)

    # === Pa-gyo ===
    # Contains ぱぴぷぺぽ　ぴゃぴゅぴぇぴょ　ぷぁぷぃぷぇぷぉ

    c_p_filter = Pedalboard([
        Gain(-15),
        PeakFilter(1000, 15, 1000 / 500),
        HighShelfFilter(6000, -35)
    ])
    c_p = c_p_filter(white_noise_base, sample_rate) * plosive_env

    c_py_filter = Pedalboard([
        Gain(-15),
        PeakFilter(1750, 14, 1750 / 750),
        HighShelfFilter(7500, -35)
    ])
    c_py = c_py_filter(white_noise_base, sample_rate) * plosive_env

    s_pa = c_p + ms_a;   s_pi = c_py + ms_i; s_pu = c_p + ms_u;   s_pe = c_p + ms_e;   s_po = c_p + ms_o
    s_pya = c_py + m_ya;                     s_pyu = c_py + m_yu; s_pye = c_py + m_ye; s_pyo = c_py + m_yo
    s_pwa = c_p + m_wa;  s_pwi = c_p + m_wi;                      s_pwe = c_p + m_we;  s_pwo = c_p + m_wo
    if not skip_pa_gyo:
        tc.save(c_p, 'p', oto_plosives_alone.as_name(''))
        tc.save(c_py, 'py', oto_plosives_alone.as_name(''))
        tc.save(s_pa, 'pa', oto_plosives.as_name('ぱ'), True)
        tc.save(s_pi, 'pi', oto_plosives.as_name('ぴ'), True)
        tc.save(s_pu, 'pu', oto_plosives.as_name('ぷ'), True)
        tc.save(s_pe, 'pe', oto_plosives.as_name('ぺ'), True)
        tc.save(s_po, 'po', oto_plosives.as_name('ぽ'), True)
        tc.save(s_pya, 'pya', oto_plosives.as_name('ぴゃ'), True)
        tc.save(s_pyu, 'pyu', oto_plosives.as_name('ぴゅ'), True)
        tc.save(s_pye, 'pye', oto_plosives.as_name('ぴぇ'), True)
        tc.save(s_pyo, 'pyo', oto_plosives.as_name('ぴょ'), True)
        tc.save(s_pwa, 'pwa', oto_plosives.as_name('ぷぁ'), True)
        tc.save(s_pwi, 'pwi', oto_plosives.as_name('ぷぃ'), True)
        tc.save(s_pwe, 'pwe', oto_plosives.as_name('ぷぇ'), True)
        tc.save(s_pwo, 'pwo', oto_plosives.as_name('ぷぉ'), True)

    # === Ba-gyo ===
    # Contains ばびぶべぼ　びゃびゅびぇびょ　ぶぁぶぃぶぇぶぉ

    c_b = c_p_filter(voiced_noise_base, sample_rate) * plosive_env
    c_by = c_py_filter(voiced_noise_base, sample_rate) * plosive_env

    s_ba = c_b + ms_a;   s_bi = c_by + ms_i; s_bu = c_b + ms_u;   s_be = c_b + ms_e;   s_bo = c_b + ms_o
    s_bya = c_by + m_ya;                     s_byu = c_by + m_yu; s_bye = c_by + m_ye; s_byo = c_by + m_yo
    s_bwa = c_b + m_wa;  s_bwi = c_b + m_wi;                      s_bwe = c_b + m_we;  s_bwo = c_b + m_wo
    if not skip_ba_gyo:
        tc.save(c_b, 'b', oto_plosives_alone.as_name(''))
        tc.save(c_by, 'by', oto_plosives_alone.as_name(''))
        tc.save(s_ba, 'ba', oto_plosives.as_name('ば'), True)
        tc.save(s_bi, 'bi', oto_plosives.as_name('び'), True)
        tc.save(s_bu, 'bu', oto_plosives.as_name('ぶ'), True)
        tc.save(s_be, 'be', oto_plosives.as_name('べ'), True)
        tc.save(s_bo, 'bo', oto_plosives.as_name('ぼ'), True)
        tc.save(s_bya, 'bya', oto_plosives.as_name('びゃ'), True)
        tc.save(s_byu, 'byu', oto_plosives.as_name('びゅ'), True)
        tc.save(s_bye, 'bye', oto_plosives.as_name('びぇ'), True)
        tc.save(s_byo, 'byo', oto_plosives.as_name('びょ'), True)
        tc.save(s_bwa, 'bwa', oto_plosives.as_name('ぷぁ'), True)
        tc.save(s_bwi, 'bwi', oto_plosives.as_name('ぷぃ'), True)
        tc.save(s_bwe, 'bwe', oto_plosives.as_name('ぷぇ'), True)
        tc.save(s_bwo, 'bwo', oto_plosives.as_name('ぷぉ'), True)

    # === Ma-gyo ===
    # Contains まみむめも　みゃみゅみぇみょ　むぁむぃむぇむぉ

    c_m = v_m * affricate_env

    s_ma = c_m + ms_a;  s_mi = c_m + ms_i;  s_mu = c_m + ms_u;  s_me = c_m + ms_e; s_mo = c_m + ms_o
    s_mya = c_m + m_ya;                     s_myu = c_m + m_yu; s_mye = c_m + m_ye; s_myo = c_m + m_yo
    s_mwa = c_m + m_wa; s_mwi = c_m + m_wi;                     s_mwe = c_m + m_we; s_mwo = c_m + m_wo
    if not skip_ma_gyo:
        tc.save(c_m, 'm_', oto_nasal_taps_alone.as_name(''))
        tc.save(s_ma, 'ma', oto_nasal_taps.as_name('ま'), True)
        tc.save(s_mi, 'mi', oto_nasal_taps.as_name('み'), True)
        tc.save(s_mu, 'mu', oto_nasal_taps.as_name('む'), True)
        tc.save(s_me, 'me', oto_nasal_taps.as_name('め'), True)
        tc.save(s_mo, 'mo', oto_nasal_taps.as_name('も'), True)
        tc.save(s_mya, 'mya', oto_nasal_taps.as_name('みゃ'), True)
        tc.save(s_myu, 'myu', oto_nasal_taps.as_name('みゅ'), True)
        tc.save(s_mye, 'mye', oto_nasal_taps.as_name('みぇ'), True)
        tc.save(s_myo, 'myo', oto_nasal_taps.as_name('みょ'), True)
        tc.save(s_mwa, 'mwa', oto_nasal_taps.as_name('むぁ'), True)
        tc.save(s_mwi, 'mwi', oto_nasal_taps.as_name('むぃ'), True)
        tc.save(s_mwe, 'mwe', oto_nasal_taps.as_name('むぇ'), True)
        tc.save(s_mwo, 'mwo', oto_nasal_taps.as_name('むぉ'), True)

    # === Ra-gyo ===
    # Contains らりるれろ　りゃりゅりぇりょ　るぁるぃるぇるぉ

    c_r = v_r * affricate_env

    s_ra = c_r + ms_a;  s_ri = c_r + ms_i;  s_ru = c_r + ms_u;  s_re = c_r + ms_e;  s_ro = c_r + ms_o
    s_rya = c_r + m_ya;                     s_ryu = c_r + m_yu; s_rye = c_r + m_ye; s_ryo = c_r + m_yo
    s_rwa = c_r + m_wa; s_rwi = c_r + m_wi;                     s_rwe = c_r + m_we; s_rwo = c_r + m_wo
    if not skip_ra_gyo:
        tc.save(c_r, 'r', oto_nasal_taps_alone.as_name(''))
        tc.save(s_ra, 'ra', oto_nasal_taps.as_name('ら'), True)
        tc.save(s_ri, 'ri', oto_nasal_taps.as_name('り'), True)
        tc.save(s_ru, 'ru', oto_nasal_taps.as_name('る'), True)
        tc.save(s_re, 're', oto_nasal_taps.as_name('れ'), True)
        tc.save(s_ro, 'ro', oto_nasal_taps.as_name('ろ'), True)
        tc.save(s_rya, 'rya', oto_nasal_taps.as_name('りゃ'), True)
        tc.save(s_ryu, 'ryu', oto_nasal_taps.as_name('りゅ'), True)
        tc.save(s_rye, 'rye', oto_nasal_taps.as_name('りぇ'), True)
        tc.save(s_ryo, 'ryo', oto_nasal_taps.as_name('りょ'), True)
        tc.save(s_rwa, 'rwa', oto_nasal_taps.as_name('るぁ'), True)
        tc.save(s_rwi, 'rwi', oto_nasal_taps.as_name('るぃ'), True)
        tc.save(s_rwe, 'rwe', oto_nasal_taps.as_name('るぇ'), True)
        tc.save(s_rwo, 'rwo', oto_nasal_taps.as_name('るぉ'), True)

    # === Extras ===
    # Contains syllables that won't happen in typical Japanese language, including
    # - Va-gyo containing ヴぁヴぃヴヴぇヴぉ, which counters to Fu syllables;
    # - Nga-gyo containing ガギグゲゴギャギュギェギョ, which are basically nasalized g- sounds
    # - Breathing sounds containing 息1/2/3, aliased as br1/2/3, each deeper with greater index

    c_v = c_f_filter(voiced_noise_base, sample_rate) * fricative_env
    c_ng = v_ng * affricate_env

    x_br1_filter = Pedalboard([
        Gain(-14),
        PeakFilter(2000, 8, 2000 / 1000),
        PeakFilter(6000, 4, 6000 / 3000),
        HighShelfFilter(10000, -45)
    ])
    x_br1 = x_br1_filter(white_noise_base, sample_rate) * np.exp(-1000 * (tvar - 0.08) ** 2)
    oto_br1 = OtoEntry('息1', 20.0, 105.0, 875.0, 20.0, 5.0)

    x_br2_filter = Pedalboard([
        Gain(-14),
        PeakFilter(1900, 8, 1900 / 1000),
        PeakFilter(5800, 4, 5800 / 3000),
        HighShelfFilter(9200, -47)
    ])
    x_br2 = x_br2_filter(white_noise_base, sample_rate) * np.exp(-300 * (tvar - 0.15) ** 2)
    oto_br2 = OtoEntry('息2', 40.0, 200.0, 760.0, 20.0, 5.0)

    x_br3_filter = Pedalboard([
        Gain(-13),
        PeakFilter(1800, 8, 1800 / 1000),
        PeakFilter(5500, 4, 5500 / 3000),
        HighShelfFilter(8700, -49)
    ])
    x_br3 = x_br3_filter(white_noise_base, sample_rate) * np.exp(-190 * (tvar - 0.19) ** 2)
    oto_br3 = OtoEntry('息3', 60.0, 250.0, 690.0, 20.0, 5.0)

    s_va = c_v + mf_a;    s_vi = c_v + mf_i;   s_vu = c_v + mf_u;    s_ve = c_v + mf_e;    s_vo = c_v + mf_o
    s_nga = c_ng + mf_a;  s_ngi = c_ng + mf_i; s_ngu = c_ng + mf_u;  s_nge = c_ng + mf_e;  s_ngo = c_ng + mf_o
    s_ngya = c_ng + m_ya;                      s_ngyu = c_ng + m_yu; s_ngye = c_ng + m_ye; s_ngyo = c_ng + m_yo
    if not skip_extras:
        tc.save(c_v, 'v', oto_fricatives_alone.as_name(''))
        tc.save(c_ng, 'ng_', oto_nasal_taps_alone.as_name(''))
        tc.save(s_va, 'va', oto_fricatives.as_name('ヴぁ'), True)
        tc.save(s_vi, 'vi', oto_fricatives.as_name('ヴぃ'), True)
        tc.save(s_vu, 'vu', oto_fricatives.as_name('ヴ'), True)
        tc.save(s_ve, 've', oto_fricatives.as_name('ヴぇ'), True)
        tc.save(s_vo, 'vo', oto_fricatives.as_name('ヴぉ'), True)
        tc.save(s_nga, 'nga', oto_nasal_taps.as_name('ガ'), True)
        tc.save(s_ngi, 'ngi', oto_nasal_taps.as_name('ギ'), True)
        tc.save(s_ngu, 'ngu', oto_nasal_taps.as_name('グ'), True)
        tc.save(s_nge, 'nge', oto_nasal_taps.as_name('ゲ'), True)
        tc.save(s_ngo, 'ngo', oto_nasal_taps.as_name('ゴ'), True)
        tc.save(s_ngya, 'ngya', oto_nasal_taps.as_name('ギャ'), True)
        tc.save(s_ngyu, 'ngyu', oto_nasal_taps.as_name('ギュ'), True)
        tc.save(s_ngye, 'ngye', oto_nasal_taps.as_name('ギェ'), True)
        tc.save(s_ngyo, 'ngyo', oto_nasal_taps.as_name('ギョ'), True)
        tc.save(x_br1, 'br1', oto_br1, True)
        tc.save(x_br2, 'br2', oto_br2, True)
        tc.save(x_br3, 'br3', oto_br3, True)

    print(f'[Info] {tc.save_count} files saved/overwritten successfully.')
    tc.save_oto()

    config = {
        'text_file_encoding': 'utf-8',
        'name': 'Technebit β1.0 Ja-CV',
        'localized_names': {
            'ja-JP': 'テクネビット β1.0 日本語-CV',
            'zh-CN': '锝比特 β1.0 日语-CV',
            'zh-TW': '鍀比特 β1.0 日語-CV'
        },
        'author': 'Generated soundbank - Python program by Nomani',
        'voice': 'FM Synthesizer (literally)',
        'version': 'β1.0',
        'web': 'https://github.com/Nomani-int64/Technebit',
        'image': {
            'base': 'image_beta_ja_cv_b1.0.png',
            'overlay': {
                'text': 'Tcb Ja-CV\nb1.0',
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
                'text': 'Technebit Ja-CV b1.0\nGen time {t}\n{s}',
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
