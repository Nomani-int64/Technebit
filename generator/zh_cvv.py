from tc_utils import *

def generate():
    '''
    Generates the entire Chinese CVV (October) soundbank. Should and onle be called once.

    The syllable names mainly refers to Hanyu Pinyin Fang'an (Chinese Phonetic Alphabet), with some features listed below:
    - Some notations are to differentiate phonological variants, such as ay = a as in ai/an;
    - The common workaround that ü is notated as v.

    The variable prefixes are as follows:
    - v_ variables are standalone vowels and nasals;
    - vc_ variables are vowel or vowel-nasal clusters;
    - c_ variables are standalone consonants;
    - m_ variables are connecting vowels or vowel clusters;
    - s_ variables are complete syllables and are ready to export;
    - x_ variables are for extra sounds;
    - oto_ variables are, obviously, oto entries.
    '''

    start_time = time.time()

    t = 1.0
    base_freq = 220.0
    sample_rate = 44100

    tc = Tc(sample_rate, base_freq, '\0Tcb b1.0 ZhCVV', True)
    tvar = np.linspace(0.0, t, int(t * sample_rate), False)

    # Skip flags
    skip_aoe = False
    skip_aieiao = False
    skip_bo, skip_po, skip_mo, skip_fo = False, False, False, False
    skip_de, skip_te, skip_ne, skip_le = False, False, False, False
    skip_ge, skip_ke, skip_he = False, False, False
    skip_ji, skip_qi, skip_xi = False, False, False
    skip_zhi, skip_chi, skip_shi, skip_ri = False, False, False, False
    skip_zi, skip_ci, skip_si = False, False, False
    skip_extras = False

    # === Vowels and nasals ===
    vowel_env = (1 - np.exp(-27 * tvar) - np.exp(27 * (tvar - t))) * (0.75 + np.exp(-15 * tvar))
    vowel_filters = Pedalboard([
        PeakFilter(220, -20, 220 / 40),
        PeakFilter(660, -15, 660 / 30),
        PeakFilter(1500, -7.5, 660 / 720),
        Gain(5)
    ])

    if True: # This indentation is for folding
        v_a = 0.3 * tc.sine(t, 5, 2 * tc.sine(t, 1)) \
            + 0.02 * tc.sine(t, 15, 8 * tc.sine(t, 1)) \
            + 0.01 * tc.sine(t, 21, 3 * tc.sine(t, 1)) \
            + 0.004 * tc.sine(t, 26, 4 * tc.sine(t, 1, 8 * tc.sine(t, 1)))
        v_a = vowel_filters(v_a, sample_rate) # a as in a/ia/ang

        v_ay = 0.28 * tc.sine(t, 6, 2.5 * tc.sine(t, 1)) \
            + 0.02 * tc.sine(t, 15, 7 * tc.sine(t, 1)) \
            + 0.004 * tc.sine(t, 24, 2 * tc.sine(t, 1)) \
            + 0.001 * tc.sine(t, 36, 3 * tc.sine(t, 1, 5 * tc.sine(t, 1)))
        v_ay = vowel_filters(v_ay, sample_rate) # a as in ai/an

        v_o = 0.3 * tc.sine(t, 2, 3 * tc.sine(t, 1)) \
            + 0.07 * tc.sine(t, 2, 5 * tc.sine(t, 1)) \
            + 0.015 * tc.sine(t, 21, 1.8 * tc.sine(t, 1)) \
            + 0.002 * tc.sine(t, 24, 4 * tc.sine(t, 1, 8 * tc.sine(t, 1)))
        v_o = vowel_filters(v_o, sample_rate) # o as in o/ou/uo

        v_ow = 0.3 * tc.sine(t, 1, 3.2 * tc.sine(t, 1)) \
            + 0.02 * tc.sine(t, 2, 3 * tc.sine(t, 1)) \
            + 0.007 * tc.sine(t, 20, 2 * tc.sine(t, 1)) \
            + 0.001 * tc.sine(t, 24, 3 * tc.sine(t, 1, 5 * tc.sine(t, 1)))
        v_ow = vowel_filters(v_ow, sample_rate) # o as in ao/ong

        v_e = 0.3 * tc.sine(t, 2, 2 * tc.sine(t, 1)) \
            + 0.06 * tc.sine(t, 7, 1.6 * tc.sine(t, 1)) \
            + 0.005 * tc.sine(t, 20, 2.7 * tc.sine(t, 1)) \
            + 0.002 * tc.sine(t, 36, 2 * tc.sine(t, 1, 5 * tc.sine(t, 1)))
        v_e = vowel_filters(v_e, sample_rate) # e as in e/en/eng/er

        v_ey = 0.2 * tc.sine(t, 2, 2.5 * tc.sine(t, 1)) \
            + 0.06 * tc.sine(t, 16, 4.5 * tc.sine(t, 1)) \
            + 0.006 * tc.sine(t, 32, 1.7 * tc.sine(t, 1)) \
            + 0.0025 * tc.sine(t, 45, 4 * tc.sine(t, 1, 4 * tc.sine(t, 1)))
        v_ey = vowel_filters(v_ey, sample_rate) # e as in ei/ie, a as in ian

        v_i = 0.27 * tc.sine(t, 1, 1.6 * tc.sine(t, 1)) \
            + 0.03 * tc.sine(t, 19, 4.5 * tc.sine(t, 1)) \
            + 0.007 * tc.sine(t, 32, 1.7 * tc.sine(t, 1)) \
            + 0.003 * tc.sine(t, 35, 4 * tc.sine(t, 1, 7 * tc.sine(t, 1)))
        v_i = vowel_filters(v_i, sample_rate) # i as in i/ia/ai

        v_u = 0.36 * tc.sine(t, 1, 2.4 * tc.sine(t, 1)) \
            + 0.008 * tc.sine(t, 16, 2 * tc.sine(t, 1)) \
            + 0.002 * tc.sine(t, 20, 2.4 * tc.sine(t, 1)) \
            + 0.0001 * tc.sine(t, 28, 3 * tc.sine(t, 1, 4 * tc.sine(t, 1)))
        v_u = vowel_filters(v_u, sample_rate) # u as in u/ua/ou

        v_v = 0.3 * tc.sine(t, 1, 1.8 * tc.sine(t, 1)) \
            + 0.08 * tc.sine(t, 13, 2.2 * tc.sine(t, 1)) \
            + 0.007 * tc.sine(t, 18, 2.2 * tc.sine(t, 1)) \
            + 0.001 * tc.sine(t, 30, 3 * tc.sine(t, 1, 3 * tc.sine(t, 1)))
        v_v = vowel_filters(v_v, sample_rate) # ü as in ü/lü, u as in ju/yu/yue

        v_iz = 0.24 * tc.sine(t, 1, 3 * tc.sine(t, 1)) \
            + 0.04 * tc.sine(t, 8, 2 * tc.sine(t, 1)) \
            + 0.01 * tc.sine(t, 20, 4 * tc.sine(t, 1)) \
            + 0.0009 * tc.sine(t, 32, 3 * tc.sine(t, 1, 2 * tc.sine(t, 1)))
        v_iz = vowel_filters(v_iz, sample_rate) # i as in zi/ci/si

        v_ir = 0.3 * tc.sine(t, 1, 2.3 * tc.sine(t, 1)) \
            + 0.06 * tc.sine(t, 10, 2.3 * tc.sine(t, 1)) \
            + 0.015 * tc.sine(t, 18, 3 * tc.sine(t, 1)) \
            + 0.0012 * tc.sine(t, 34, 3 * tc.sine(t, 1, 2.5 * tc.sine(t, 1)))
        v_ir = vowel_filters(v_ir, sample_rate) # i as in zhi/chi/shi/ri

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
            + 0.05 * tc.sine(t, 8, 3 * tc.sine(t, 1)) \
            + 0.01 * tc.sine(t, 15, 3 * tc.sine(t, 1))
        v_l = vowel_filters(v_l, sample_rate)

    oto_vowels = OtoEntry('', 0.0, 300.0, 200.0, 25.0, 10.0)

    if not skip_aoe:
        tc.save(v_a * vowel_env, 'a', oto_vowels)
        tc.save(v_o * vowel_env, 'o', oto_vowels)
        tc.save(v_e * vowel_env, 'e', oto_vowels)
        tc.save(v_i * vowel_env, 'yi', oto_vowels)
        tc.save(v_u * vowel_env, 'wu', oto_vowels)
        tc.save(v_v * vowel_env, 'yu', oto_vowels)
        tc.save(v_m * vowel_env, 'm', oto_vowels)
        tc.save(v_n * vowel_env, 'n', oto_vowels)
        tc.save(v_ng * vowel_env, 'ng', oto_vowels)

    # === Vowel and vowel-nasal clusters ===
    # Very cursed yet efficient way to glue vowels together
    # Like, what the hell's happening here, but OMG it worked!
    fast_clust_1_env = np.exp(-13 * tvar)
    fast_clust_2_env = 0.5 * np.exp(-(2.8 + np.log(tvar + 1e-10)) ** 2)
    fast_clust_3_env = 1 - np.exp(-12 * tvar)
    fast_clust = lambda w1, w2, w3: fast_clust_1_env * w1 + fast_clust_2_env * w2 + fast_clust_3_env * w3

    slow_clust_1_env = (1 - np.exp(-25 * (tvar - 0.8) ** 2)) * (tvar < 0.8)
    slow_clust_2_env = 0.75 * np.exp(-75 * (tvar - 0.7) ** 2)
    slow_clust_3_env = (1 - np.exp(-30 * (tvar - 0.65) ** 2)) * (tvar > 0.65)
    slow_clust = lambda w1, w2, w3: slow_clust_1_env * w1 + slow_clust_2_env * w2 + slow_clust_3_env * w3

    quad_clust_2_env = (1 - np.exp(-85 * tvar ** 2)) * (1 - np.exp(-25 * (tvar - 0.8) ** 2)) * (tvar < 0.8)
    quad_clust = lambda w1, w2, w3, w4: fast_clust_1_env * w1 + quad_clust_2_env * w2 + slow_clust_2_env * w3 + slow_clust_3_env * w4

    if True:
        vc_ai = slow_clust(v_ay, v_ey, v_i)
        vc_ei = slow_clust(v_ey, v_ey, v_i)
        vc_ao = slow_clust(v_a, v_o, v_ow)
        vc_ou = slow_clust(v_o, v_ow, v_u)
        vc_ve = slow_clust(v_v, v_iz, v_ey)
        vc_er = slow_clust(v_e, v_e, v_ir)

        vc_an = slow_clust(v_ay, v_ay, v_n)
        vc_en = slow_clust(v_e, v_e, v_n)
        vc_in = slow_clust(v_i, v_i, v_n)
        vc_vn = slow_clust(v_v, v_i, v_n)
        vc_van = quad_clust(v_v, v_ey, v_ey, v_n)

        vc_ang = slow_clust(v_a, v_a, v_ng)
        vc_eng = slow_clust(v_e, v_e, v_ng)
        vc_ing = slow_clust(v_i, v_i, v_ng)
        vc_ong = slow_clust(v_o, v_ow, v_ng)

        vc_ia = fast_clust(v_i, v_ey, v_a)
        vc_ie = fast_clust(v_i, v_ey, v_ey)
        vc_iao = quad_clust(v_i, v_a, v_o, v_ow)
        vc_iou = quad_clust(v_i, v_o, v_ow, v_u)
        vc_ian = quad_clust(v_i, v_ey, v_ey, v_n)
        vc_iang = quad_clust(v_i, v_a, v_a, v_ng)
        vc_iong = quad_clust(v_i, v_o, v_ow, v_ng)

        vc_ua = fast_clust(v_u, v_o, v_a)
        vc_uo = fast_clust(v_u, v_ow, v_o)
        vc_uai = quad_clust(v_u, v_ay, v_ey, v_i)
        vc_uei = quad_clust(v_u, v_ey, v_ey, v_i)
        vc_uan = quad_clust(v_u, v_ay, v_e, v_n)
        vc_uen = quad_clust(v_u, v_e, v_e, v_n)
        vc_uang = quad_clust(v_u, v_a, v_a, v_ng)
        vc_ueng = quad_clust(v_u, v_e, v_e, v_ng)

    oto_clusters = OtoEntry('', 0.0, 300.0, 200.0, 30.0, 10.0)
    oto_clusters_expand = lambda cl: [_oto % cl for _oto in [
        OtoEntry('', 0.0, 300.0, 420.0, 30.0, 10.0),
        OtoEntry('_%s', 750.0, 200.0, 5.0, 50.0, 100.0)
    ]]
    oto_clusters_trunc = OtoEntry('', 0.0, 300.0, 420.0, 30.0, 10.0)

    if not skip_aieiao:
        tc.save_sep(vc_ai * vowel_env, 'ai', oto_clusters_expand('ai'))
        tc.save_sep(vc_ei * vowel_env, 'ei', oto_clusters_expand('ei'))
        tc.save_sep(vc_ao * vowel_env, 'ao', oto_clusters_expand('ao'))
        tc.save_sep(vc_ou * vowel_env, 'ou', oto_clusters_expand('ou'))
        tc.save_sep(vc_ve * vowel_env, 'yue', oto_clusters)
        tc.save_sep(vc_er * vowel_env, 'er', oto_clusters)
        tc.save_sep(vc_an * vowel_env, 'an', oto_clusters_expand('an'))
        tc.save_sep(vc_en * vowel_env, 'en', oto_clusters_expand('en'))
        tc.save_sep(vc_in * vowel_env, 'yin', oto_clusters_expand('in'))
        tc.save_sep(vc_vn * vowel_env, 'yun', oto_clusters_expand('vn'))
        tc.save_sep(vc_van * vowel_env, 'yuan', oto_clusters_trunc)
        tc.save_sep(vc_ang * vowel_env, 'ang', oto_clusters_expand('ang'))
        tc.save_sep(vc_eng * vowel_env, 'eng', oto_clusters_expand('eng'))
        tc.save_sep(vc_ing * vowel_env, 'ying', oto_clusters_expand('ing'))
        tc.save_sep(vc_ong * vowel_env, 'ong', oto_clusters_expand('ong'))
        tc.save_sep(vc_ia * vowel_env, 'ya', oto_clusters)
        tc.save_sep(vc_ie * vowel_env, 'ye', oto_clusters)
        tc.save_sep(vc_iao * vowel_env, 'yao', oto_clusters_trunc)
        tc.save_sep(vc_iou * vowel_env, 'you', oto_clusters_trunc)
        tc.save_sep(vc_ian * vowel_env, 'yan', oto_clusters_expand('en2'))
        tc.save_sep(vc_iang * vowel_env, 'yang', oto_clusters_trunc)
        tc.save_sep(vc_iong * vowel_env, 'yong', oto_clusters_trunc)
        tc.save_sep(vc_ua * vowel_env, 'wa', oto_clusters)
        tc.save_sep(vc_uo * vowel_env, 'wo', oto_clusters)
        tc.save_sep(vc_uai * vowel_env, 'wai', oto_clusters_expand('uai'))
        tc.save_sep(vc_uei * vowel_env, 'wei', oto_clusters_trunc)
        tc.save_sep(vc_uan * vowel_env, 'wan', oto_clusters_trunc)
        tc.save_sep(vc_uen * vowel_env, 'wen', oto_clusters_expand('un'))
        tc.save_sep(vc_uang * vowel_env, 'wang', oto_clusters_trunc)
        tc.save_sep(vc_ueng * vowel_env, 'weng', oto_clusters_trunc)

    # === Multiplexes ===

    vowel_env_plos = 1 - np.clip(np.exp(-18 * (tvar - 0.0075)), 0, 1) ** 2 - np.exp(27 * (tvar - t))
    vowel_env_frict = (1 - np.exp(-18 * (tvar - 0.01)) - np.exp(27 * (tvar - t))) * (0.5 + np.arctan(50 * (tvar - 0.03)) / np.pi)
    cluster_env_concat = 1 - np.exp(-27 * tvar) - np.clip(np.exp(27 * (tvar - t + 0.01)), 0, 1)
    vplos_cat = lambda c, v: c + v * vowel_env_plos
    vfrict_cat = lambda c, v: c + v * vowel_env_frict
    clust_cat = lambda c, vc: tc.shift_add(c, vc * cluster_env_concat, 0.01)

    white_noise_base = tc.noise(t) * 1.25
    voiced_noise_base = tc.noise(t) * 0.4 + tc.saw(t, 1) * 0.75
    plosive_env = np.exp(-(4.5 + np.log(tvar + 1e-10)) ** 2) * 1.2
    fricative_env = np.clip(1 - np.exp(-300 * tvar) - np.exp(100 * (tvar - 0.055)), 0, 1) * 0.7
    affricate_env = np.sqrt(plosive_env * fricative_env) * 0.8

    oto_plosives = OtoEntry('', 4.0, 300.0, 200.0, 30.0, 5.0)
    oto_fricatives = OtoEntry('', 0.0, 300.0, 200.0, 30.0, 15.0)
    oto_affricates = OtoEntry('', 4.0, 300.0, 200.0, 30.0, 5.0)
    oto_nasal_taps = OtoEntry('', 0.0, 300.0, 200.0, 30.0, 15.0)
    oto_plosives_trunc = OtoEntry('', 4.0, 300.0, 420.0, 30.0, 5.0)
    oto_fricatives_trunc = OtoEntry('', 0.0, 300.0, 420.0, 30.0, 15.0)
    oto_affricates_trunc = OtoEntry('', 4.0, 300.0, 420.0, 30.0, 5.0)
    oto_nasal_taps_trunc = OtoEntry('', 0.0, 300.0, 420.0, 30.0, 15.0)
    oto_plosives_alone = OtoEntry('', 4.0, 120.0, 880.0, 15.0, 5.0)
    oto_fricatives_alone = OtoEntry('', 0.0, 30.0, 950.0, 15.0, 10.0)
    oto_affricates_alone = OtoEntry('', 4.0, 55.0, 945.0, 15.0, 5.0)
    oto_nasal_taps_alone = OtoEntry('', 0.0, 50.0, 950.0, 15.0, 10.0)

    # === Bo ===

    c_p_filter = Pedalboard([
        Gain(-15),
        PeakFilter(1000, 15, 1000 / 500),
        HighShelfFilter(6000, -35)
    ])
    c_b = c_p_filter(voiced_noise_base, sample_rate) * plosive_env

    c_py_filter = Pedalboard([
        Gain(-15),
        PeakFilter(1750, 14, 1750 / 750),
        HighShelfFilter(7500, -35)
    ])
    c_by = c_py_filter(voiced_noise_base, sample_rate) * plosive_env

    if True:
        s_ba = vplos_cat(c_b, v_a)
        s_bo = vplos_cat(c_b, v_o)
        s_bi = vplos_cat(c_by, v_i)
        s_bu = vplos_cat(c_b, v_u)
        s_bai = vplos_cat(c_b, vc_ai)
        s_bei = vplos_cat(c_by, vc_ei)
        s_bao = vplos_cat(c_b, vc_ao)
        s_ban = vplos_cat(c_b, vc_an)
        s_ben = vplos_cat(c_b, vc_en)
        s_bin = vplos_cat(c_by, vc_in)
        s_bang = vplos_cat(c_b, vc_ang)
        s_beng = vplos_cat(c_b, vc_eng)
        s_bing = vplos_cat(c_by, vc_ing)
        s_bie = clust_cat(c_by, vc_ie)
        s_biao = clust_cat(c_by, vc_iao)
        s_bian = clust_cat(c_by, vc_ian)

    if not skip_bo:
        tc.save(c_b, 'b', oto_plosives_alone)
        tc.save(c_by, 'by', oto_plosives_alone)
        tc.save(s_ba, 'ba', oto_plosives)
        tc.save(s_bo, 'bo', oto_plosives)
        tc.save(s_bi, 'bi', oto_plosives)
        tc.save(s_bu, 'bu', oto_plosives)
        tc.save(s_bai, 'bai', oto_plosives_trunc)
        tc.save(s_bei, 'bei', oto_plosives_trunc)
        tc.save(s_bao, 'bao', oto_plosives_trunc)
        tc.save(s_ban, 'ban', oto_plosives_trunc)
        tc.save(s_ben, 'ben', oto_plosives_trunc)
        tc.save(s_bin, 'bin', oto_plosives_trunc)
        tc.save(s_bang, 'bang', oto_plosives_trunc)
        tc.save(s_beng, 'beng', oto_plosives_trunc)
        tc.save(s_bing, 'bing', oto_plosives_trunc)
        tc.save(s_bie, 'bie', oto_plosives)
        tc.save(s_biao, 'biao', oto_plosives_trunc)
        tc.save(s_bian, 'bian', oto_plosives_trunc)

    # === Po ===

    c_p = c_p_filter(white_noise_base, sample_rate) * plosive_env
    c_py = c_py_filter(white_noise_base, sample_rate) * plosive_env

    if True:
        s_pa = vplos_cat(c_p, v_a)
        s_po = vplos_cat(c_p, v_o)
        s_pi = vplos_cat(c_py, v_i)
        s_pu = vplos_cat(c_p, v_u)
        s_pai = vplos_cat(c_p, vc_ai)
        s_pei = vplos_cat(c_py, vc_ei)
        s_pao = vplos_cat(c_p, vc_ao)
        s_pou = vplos_cat(c_p, vc_ou)
        s_pan = vplos_cat(c_p, vc_an)
        s_pen = vplos_cat(c_p, vc_en)
        s_pin = vplos_cat(c_py, vc_in)
        s_pang = vplos_cat(c_p, vc_ang)
        s_peng = vplos_cat(c_p, vc_eng)
        s_ping = vplos_cat(c_py, vc_ing)
        s_pie = clust_cat(c_py, vc_ie)
        s_piao = clust_cat(c_py, vc_iao)
        s_pian = clust_cat(c_py, vc_ian)

    if not skip_po:
        tc.save(c_p, 'p', oto_plosives_alone)
        tc.save(c_py, 'py', oto_plosives_alone)
        tc.save(s_pa, 'pa', oto_plosives)
        tc.save(s_po, 'po', oto_plosives)
        tc.save(s_pi, 'pi', oto_plosives)
        tc.save(s_pu, 'pu', oto_plosives)
        tc.save(s_pai, 'pai', oto_plosives_trunc)
        tc.save(s_pei, 'pei', oto_plosives_trunc)
        tc.save(s_pao, 'pao', oto_plosives_trunc)
        tc.save(s_pou, 'pou', oto_plosives_trunc)
        tc.save(s_pan, 'pan', oto_plosives_trunc)
        tc.save(s_pen, 'pen', oto_plosives_trunc)
        tc.save(s_pin, 'pin', oto_plosives_trunc)
        tc.save(s_pang, 'pang', oto_plosives_trunc)
        tc.save(s_peng, 'peng', oto_plosives_trunc)
        tc.save(s_ping, 'ping', oto_plosives_trunc)
        tc.save(s_pie, 'pie', oto_plosives)
        tc.save(s_piao, 'piao', oto_plosives_trunc)
        tc.save(s_pian, 'pian', oto_plosives_trunc)

    # === Mo ===

    c_m = v_m * affricate_env

    if True:
        s_ma = vfrict_cat(c_m, v_a)
        s_mo = vfrict_cat(c_m, v_o)
        s_me = vfrict_cat(c_m, v_e)
        s_mi = vfrict_cat(c_m, v_i)
        s_mu = vfrict_cat(c_m, v_u)
        s_mai = vfrict_cat(c_m, vc_ai)
        s_mei = vfrict_cat(c_m, vc_ei)
        s_mao = vfrict_cat(c_m, vc_ao)
        s_mou = vfrict_cat(c_m, vc_ou)
        s_man = vfrict_cat(c_m, vc_an)
        s_men = vfrict_cat(c_m, vc_en)
        s_min = vfrict_cat(c_m, vc_in)
        s_mang = vfrict_cat(c_m, vc_ang)
        s_meng = vfrict_cat(c_m, vc_eng)
        s_ming = vfrict_cat(c_m, vc_ing)
        s_mie = clust_cat(c_m, vc_ie)
        s_miao = clust_cat(c_m, vc_iao)
        s_mian = clust_cat(c_m, vc_ian)

    if not skip_mo:
        tc.save(c_m, 'm_', oto_nasal_taps_alone)
        tc.save(s_ma, 'ma', oto_nasal_taps)
        tc.save(s_mo, 'mo', oto_nasal_taps)
        tc.save(s_me, 'me', oto_nasal_taps)
        tc.save(s_mi, 'mi', oto_nasal_taps)
        tc.save(s_mu, 'mu', oto_nasal_taps)
        tc.save(s_mai, 'mai', oto_nasal_taps_trunc)
        tc.save(s_mei, 'mei', oto_nasal_taps_trunc)
        tc.save(s_mao, 'mao', oto_nasal_taps_trunc)
        tc.save(s_mou, 'mou', oto_nasal_taps_trunc)
        tc.save(s_man, 'man', oto_nasal_taps_trunc)
        tc.save(s_men, 'men', oto_nasal_taps_trunc)
        tc.save(s_min, 'min', oto_nasal_taps_trunc)
        tc.save(s_mang, 'mang', oto_nasal_taps_trunc)
        tc.save(s_meng, 'meng', oto_nasal_taps_trunc)
        tc.save(s_ming, 'ming', oto_nasal_taps_trunc)
        tc.save(s_mie, 'mie', oto_nasal_taps)
        tc.save(s_miao, 'miao', oto_nasal_taps_trunc)
        tc.save(s_mian, 'mian', oto_nasal_taps_trunc)

    # === Fo ===

    c_f_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1600, 12, 1600 / 900),
        PeakFilter(4000, 7, 4000 / 2500),
        HighShelfFilter(7000, -50)
    ])
    c_f = c_f_filter(white_noise_base, sample_rate) * fricative_env

    if True:
        s_fa = vfrict_cat(c_f, v_a)
        s_fo = vfrict_cat(c_f, v_o)
        s_fu = vfrict_cat(c_f, v_u)
        s_fei = vfrict_cat(c_f, vc_ei)
        s_fou = vfrict_cat(c_f, vc_ou)
        s_fan = vfrict_cat(c_f, vc_an)
        s_fen = vfrict_cat(c_f, vc_en)
        s_fang = vfrict_cat(c_f, vc_ang)
        s_feng = vfrict_cat(c_f, vc_eng)

    if not skip_fo:
        tc.save(c_f, 'f', oto_fricatives_alone)
        tc.save(s_fa, 'fa', oto_fricatives)
        tc.save(s_fo, 'fo', oto_fricatives)
        tc.save(s_fu, 'fu', oto_fricatives)
        tc.save(s_fei, 'fei', oto_fricatives_trunc)
        tc.save(s_fou, 'fou', oto_fricatives_trunc)
        tc.save(s_fan, 'fan', oto_fricatives_trunc)
        tc.save(s_fen, 'fen', oto_fricatives_trunc)
        tc.save(s_fang, 'fang', oto_fricatives_trunc)
        tc.save(s_feng, 'feng', oto_fricatives_trunc)

    # === De ===

    c_t_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1800, 18, 1800 / 1800),
        PeakFilter(5000, 8, 5000 / 3000),
        HighShelfFilter(10000, -50)
    ])
    c_d = c_t_filter(voiced_noise_base, sample_rate) * plosive_env

    c_ty_filter = Pedalboard([
        Gain(-18),
        PeakFilter(1800, 18, 1800 / 1600),
        PeakFilter(5600, 8, 5600 / 3200),
        HighShelfFilter(12000, -50)
    ])
    c_dy = c_ty_filter(voiced_noise_base, sample_rate) * plosive_env

    if True:
        s_da = vplos_cat(c_d, v_a)
        s_de = vplos_cat(c_d, v_e)
        s_di = vplos_cat(c_dy, v_i)
        s_du = vplos_cat(c_d, v_u)
        s_dai = vplos_cat(c_d, vc_ai)
        s_dei = vplos_cat(c_dy, vc_ei)
        s_dao = vplos_cat(c_d, vc_ao)
        s_dou = vplos_cat(c_d, vc_ou)
        s_dan = vplos_cat(c_d, vc_an)
        s_den = vplos_cat(c_d, vc_en)
        s_dang = vplos_cat(c_d, vc_ang)
        s_deng = vplos_cat(c_d, vc_eng)
        s_ding = vplos_cat(c_dy, vc_ing)
        s_dong = vplos_cat(c_d, vc_ong)
        s_die = clust_cat(c_dy, vc_ie)
        s_diao = clust_cat(c_dy, vc_iao)
        s_diu = clust_cat(c_dy, vc_iou)
        s_dian = clust_cat(c_dy, vc_ian)
        s_duo = clust_cat(c_d, vc_uo)
        s_dui = clust_cat(c_d, vc_uei)
        s_duan = clust_cat(c_d, vc_uan)
        s_dun = clust_cat(c_d, vc_uen)

    if not skip_de:
        tc.save(c_d, 'd', oto_plosives_alone)
        tc.save(c_dy, 'dy', oto_plosives_alone)
        tc.save(s_da, 'da', oto_plosives)
        tc.save(s_de, 'de', oto_plosives)
        tc.save(s_di, 'di', oto_plosives)
        tc.save(s_du, 'du', oto_plosives)
        tc.save(s_dai, 'dai', oto_plosives_trunc)
        tc.save(s_dei, 'dei', oto_plosives_trunc)
        tc.save(s_dao, 'dao', oto_plosives_trunc)
        tc.save(s_dou, 'dou', oto_plosives_trunc)
        tc.save(s_dan, 'dan', oto_plosives_trunc)
        tc.save(s_den, 'den', oto_plosives_trunc)
        tc.save(s_dang, 'dang', oto_plosives_trunc)
        tc.save(s_deng, 'deng', oto_plosives_trunc)
        tc.save(s_ding, 'ding', oto_plosives_trunc)
        tc.save(s_dong, 'dong', oto_plosives_trunc)
        tc.save(s_die, 'die', oto_plosives)
        tc.save(s_diao, 'diao', oto_plosives_trunc)
        tc.save(s_diu, 'diu', oto_plosives_trunc)
        tc.save(s_dian, 'dian', oto_plosives_trunc)
        tc.save(s_duo, 'duo', oto_plosives)
        tc.save(s_dui, 'dui', oto_plosives_trunc)
        tc.save(s_duan, 'duan', oto_plosives_trunc)
        tc.save(s_dun, 'dun', oto_plosives_trunc)

    # === Te ===

    c_t = c_t_filter(white_noise_base, sample_rate) * plosive_env
    c_ty = c_ty_filter(white_noise_base, sample_rate) * plosive_env

    if True:
        s_ta = vplos_cat(c_t, v_a)
        s_te = vplos_cat(c_t, v_e)
        s_ti = vplos_cat(c_ty, v_i)
        s_tu = vplos_cat(c_t, v_u)
        s_tai = vplos_cat(c_t, vc_ai)
        s_tei = vplos_cat(c_ty, vc_ei)
        s_tao = vplos_cat(c_t, vc_ao)
        s_tou = vplos_cat(c_t, vc_ou)
        s_tan = vplos_cat(c_t, vc_an)
        s_tang = vplos_cat(c_t, vc_ang)
        s_teng = vplos_cat(c_t, vc_eng)
        s_ting = vplos_cat(c_ty, vc_ing)
        s_tong = vplos_cat(c_t, vc_ong)
        s_tie = clust_cat(c_ty, vc_ie)
        s_tiao = clust_cat(c_ty, vc_iao)
        s_tian = clust_cat(c_ty, vc_ian)
        s_tuo = clust_cat(c_t, vc_uo)
        s_tui = clust_cat(c_t, vc_uei)
        s_tuan = clust_cat(c_t, vc_uan)
        s_tun = clust_cat(c_t, vc_uen)

    if not skip_te:
        tc.save(c_t, 't', oto_plosives_alone)
        tc.save(c_ty, 'ty', oto_plosives_alone)
        tc.save(s_ta, 'ta', oto_plosives)
        tc.save(s_te, 'te', oto_plosives)
        tc.save(s_ti, 'ti', oto_plosives)
        tc.save(s_tu, 'tu', oto_plosives)
        tc.save(s_tai, 'tai', oto_plosives_trunc)
        tc.save(s_tei, 'tei', oto_plosives_trunc)
        tc.save(s_tao, 'tao', oto_plosives_trunc)
        tc.save(s_tou, 'tou', oto_plosives_trunc)
        tc.save(s_tan, 'tan', oto_plosives_trunc)
        tc.save(s_tang, 'tang', oto_plosives_trunc)
        tc.save(s_teng, 'teng', oto_plosives_trunc)
        tc.save(s_ting, 'ting', oto_plosives_trunc)
        tc.save(s_tong, 'tong', oto_plosives_trunc)
        tc.save(s_tie, 'tie', oto_plosives)
        tc.save(s_tiao, 'tiao', oto_plosives_trunc)
        tc.save(s_tian, 'tian', oto_plosives_trunc)
        tc.save(s_tuo, 'tuo', oto_plosives)
        tc.save(s_tui, 'tui', oto_plosives_trunc)
        tc.save(s_tuan, 'tuan', oto_plosives_trunc)
        tc.save(s_tun, 'tun', oto_plosives_trunc)

    # === Ne ===

    c_n = v_n * affricate_env

    if True:
        s_na = vfrict_cat(c_n, v_a)
        s_ne = vfrict_cat(c_n, v_e)
        s_ni = vfrict_cat(c_n, v_i)
        s_nu = vfrict_cat(c_n, v_u)
        s_nv = vfrict_cat(c_n, v_v)
        s_nai = vfrict_cat(c_n, vc_ai)
        s_nei = vfrict_cat(c_n, vc_ei)
        s_nao = vfrict_cat(c_n, vc_ao)
        s_nou = vfrict_cat(c_n, vc_ou)
        s_nve = vfrict_cat(c_n, vc_ve)
        s_nan = vfrict_cat(c_n, vc_an)
        s_nen = vfrict_cat(c_n, vc_en)
        s_nin = vfrict_cat(c_n, vc_in)
        s_nang = vfrict_cat(c_n, vc_ang)
        s_neng = vfrict_cat(c_n, vc_eng)
        s_ning = vfrict_cat(c_n, vc_ing)
        s_nong = vfrict_cat(c_n, vc_ong)
        s_nie = clust_cat(c_n, vc_ie)
        s_niao = clust_cat(c_n, vc_iao)
        s_niu = clust_cat(c_n, vc_iou)
        s_nian = clust_cat(c_n, vc_ian)
        s_niang = clust_cat(c_n, vc_iang)
        s_nuo = clust_cat(c_n, vc_uo)
        s_nuan = clust_cat(c_n, vc_uan)
        s_nun = clust_cat(c_n, vc_uen)

    if not skip_ne:
        tc.save(c_n, 'n_', oto_nasal_taps_alone)
        tc.save(s_na, 'na', oto_nasal_taps)
        tc.save(s_ne, 'ne', oto_nasal_taps)
        tc.save(s_ni, 'ni', oto_nasal_taps)
        tc.save(s_nu, 'nu', oto_nasal_taps)
        tc.save(s_nv, 'nv', oto_nasal_taps)
        tc.save(s_nai, 'nai', oto_nasal_taps_trunc)
        tc.save(s_nei, 'nei', oto_nasal_taps_trunc)
        tc.save(s_nao, 'nao', oto_nasal_taps_trunc)
        tc.save(s_nou, 'nou', oto_nasal_taps_trunc)
        tc.save(s_nve, 'nve', oto_nasal_taps)
        tc.save(s_nan, 'nan', oto_nasal_taps_trunc)
        tc.save(s_nen, 'nen', oto_nasal_taps_trunc)
        tc.save(s_nin, 'nin', oto_nasal_taps_trunc)
        tc.save(s_nang, 'nang', oto_nasal_taps_trunc)
        tc.save(s_neng, 'neng', oto_nasal_taps_trunc)
        tc.save(s_ning, 'ning', oto_nasal_taps_trunc)
        tc.save(s_nong, 'nong', oto_nasal_taps_trunc)
        tc.save(s_nie, 'nie', oto_nasal_taps)
        tc.save(s_niao, 'niao', oto_nasal_taps_trunc)
        tc.save(s_niu, 'niu', oto_nasal_taps_trunc)
        tc.save(s_nian, 'nian', oto_nasal_taps_trunc)
        tc.save(s_niang, 'niang', oto_nasal_taps_trunc)
        tc.save(s_nuo, 'nuo', oto_nasal_taps)
        tc.save(s_nuan, 'nuan', oto_nasal_taps_trunc)
        tc.save(s_nun, 'nun', oto_nasal_taps_trunc)

    # === Le ===

    c_l = v_l * affricate_env

    if True:
        s_la = vfrict_cat(c_l, v_a)
        s_le = vfrict_cat(c_l, v_e)
        s_li = vfrict_cat(c_l, v_i)
        s_lu = vfrict_cat(c_l, v_u)
        s_lv = vfrict_cat(c_l, v_v)
        s_lai = vfrict_cat(c_l, vc_ai)
        s_lei = vfrict_cat(c_l, vc_ei)
        s_lao = vfrict_cat(c_l, vc_ao)
        s_lou = vfrict_cat(c_l, vc_ou)
        s_lve = vfrict_cat(c_l, vc_ve)
        s_lan = vfrict_cat(c_l, vc_an)
        s_lin = vfrict_cat(c_l, vc_in)
        s_lang = vfrict_cat(c_l, vc_ang)
        s_leng = vfrict_cat(c_l, vc_eng)
        s_ling = vfrict_cat(c_l, vc_ing)
        s_long = vfrict_cat(c_l, vc_ong)
        s_lie = clust_cat(c_l, vc_ie)
        s_liao = clust_cat(c_l, vc_iao)
        s_liu = clust_cat(c_l, vc_iou)
        s_lian = clust_cat(c_l, vc_ian)
        s_liang = clust_cat(c_l, vc_iang)
        s_luo = clust_cat(c_l, vc_uo)
        s_luan = clust_cat(c_l, vc_uan)
        s_lun = clust_cat(c_l, vc_uen)

    if not skip_le:
        tc.save(c_l, 'l', oto_nasal_taps_alone)
        tc.save(s_la, 'la', oto_nasal_taps)
        tc.save(s_le, 'le', oto_nasal_taps)
        tc.save(s_li, 'li', oto_nasal_taps)
        tc.save(s_lu, 'lu', oto_nasal_taps)
        tc.save(s_lv, 'lv', oto_nasal_taps)
        tc.save(s_lai, 'lai', oto_nasal_taps_trunc)
        tc.save(s_lei, 'lei', oto_nasal_taps_trunc)
        tc.save(s_lao, 'lao', oto_nasal_taps_trunc)
        tc.save(s_lou, 'lou', oto_nasal_taps_trunc)
        tc.save(s_lve, 'lve', oto_nasal_taps)
        tc.save(s_lan, 'lan', oto_nasal_taps_trunc)
        tc.save(s_lin, 'lin', oto_nasal_taps_trunc)
        tc.save(s_lang, 'lang', oto_nasal_taps_trunc)
        tc.save(s_leng, 'leng', oto_nasal_taps_trunc)
        tc.save(s_ling, 'ling', oto_nasal_taps_trunc)
        tc.save(s_long, 'long', oto_nasal_taps_trunc)
        tc.save(s_lie, 'lie', oto_nasal_taps)
        tc.save(s_liao, 'liao', oto_nasal_taps_trunc)
        tc.save(s_liu, 'liu', oto_nasal_taps_trunc)
        tc.save(s_lian, 'lian', oto_nasal_taps_trunc)
        tc.save(s_liang, 'liang', oto_nasal_taps_trunc)
        tc.save(s_luo, 'luo', oto_nasal_taps)
        tc.save(s_luan, 'luan', oto_nasal_taps_trunc)
        tc.save(s_lun, 'lun', oto_nasal_taps_trunc)

    # === Ge ===

    c_k_filter = Pedalboard([
            Gain(-11),
            PeakFilter(1500, 20, 2000 / 800),
            PeakFilter(5000, 11, 5000 / 1000),
            HighShelfFilter(10000, -65)
        ])
    c_g = c_k_filter(voiced_noise_base, sample_rate) * plosive_env

    if True:
        s_ga = vplos_cat(c_g, v_a)
        s_ge = vplos_cat(c_g, v_e)
        s_gu = vplos_cat(c_g, v_u)
        s_gai = vplos_cat(c_g, vc_ai)
        s_gei = vplos_cat(c_g, vc_ei)
        s_gao = vplos_cat(c_g, vc_ao)
        s_gou = vplos_cat(c_g, vc_ou)
        s_gan = vplos_cat(c_g, vc_an)
        s_gen = vplos_cat(c_g, vc_en)
        s_gang = vplos_cat(c_g, vc_ang)
        s_geng = vplos_cat(c_g, vc_eng)
        s_gong = vplos_cat(c_g, vc_ong)
        s_gua = clust_cat(c_g, vc_ua)
        s_guo = clust_cat(c_g, vc_uo)
        s_guai = clust_cat(c_g, vc_uai)
        s_gui = clust_cat(c_g, vc_uei)
        s_guan = clust_cat(c_g, vc_uan)
        s_gun = clust_cat(c_g, vc_uen)
        s_guang = clust_cat(c_g, vc_uang)

    if not skip_ge:
        tc.save(c_g, 'g', oto_plosives_alone)
        tc.save(s_ga, 'ga', oto_plosives)
        tc.save(s_ge, 'ge', oto_plosives)
        tc.save(s_gu, 'gu', oto_plosives)
        tc.save(s_gai, 'gai', oto_plosives_trunc)
        tc.save(s_gei, 'gei', oto_plosives_trunc)
        tc.save(s_gao, 'gao', oto_plosives_trunc)
        tc.save(s_gou, 'gou', oto_plosives_trunc)
        tc.save(s_gan, 'gan', oto_plosives_trunc)
        tc.save(s_gen, 'gen', oto_plosives_trunc)
        tc.save(s_gang, 'gang', oto_plosives_trunc)
        tc.save(s_geng, 'geng', oto_plosives_trunc)
        tc.save(s_gong, 'gong', oto_plosives_trunc)
        tc.save(s_gua, 'gua', oto_plosives)
        tc.save(s_guo, 'guo', oto_plosives)
        tc.save(s_guai, 'guai', oto_plosives_trunc)
        tc.save(s_gui, 'gui', oto_plosives_trunc)
        tc.save(s_guan, 'guan', oto_plosives_trunc)
        tc.save(s_gun, 'gun', oto_plosives_trunc)
        tc.save(s_guang, 'guang', oto_plosives_trunc)

    # === Ke ===

    c_k = c_k_filter(white_noise_base, sample_rate) * plosive_env

    if True:
        s_ka = vplos_cat(c_k, v_a)
        s_ke = vplos_cat(c_k, v_e)
        s_ku = vplos_cat(c_k, v_u)
        s_kai = vplos_cat(c_k, vc_ai)
        s_kei = vplos_cat(c_k, vc_ei)
        s_kao = vplos_cat(c_k, vc_ao)
        s_kou = vplos_cat(c_k, vc_ou)
        s_kan = vplos_cat(c_k, vc_an)
        s_ken = vplos_cat(c_k, vc_en)
        s_kang = vplos_cat(c_k, vc_ang)
        s_keng = vplos_cat(c_k, vc_eng)
        s_kong = vplos_cat(c_k, vc_ong)
        s_kua = clust_cat(c_k, vc_ua)
        s_kuo = clust_cat(c_k, vc_uo)
        s_kuai = clust_cat(c_k, vc_uai)
        s_kui = clust_cat(c_k, vc_uei)
        s_kuan = clust_cat(c_k, vc_uan)
        s_kun = clust_cat(c_k, vc_uen)
        s_kuang = clust_cat(c_k, vc_uang)

    if not skip_ke:
        tc.save(c_k, 'k', oto_plosives_alone)
        tc.save(s_ka, 'ka', oto_plosives)
        tc.save(s_ke, 'ke', oto_plosives)
        tc.save(s_ku, 'ku', oto_plosives)
        tc.save(s_kai, 'kai', oto_plosives_trunc)
        tc.save(s_kei, 'kei', oto_plosives_trunc)
        tc.save(s_kao, 'kao', oto_plosives_trunc)
        tc.save(s_kou, 'kou', oto_plosives_trunc)
        tc.save(s_kan, 'kan', oto_plosives_trunc)
        tc.save(s_ken, 'ken', oto_plosives_trunc)
        tc.save(s_kang, 'kang', oto_plosives_trunc)
        tc.save(s_keng, 'keng', oto_plosives_trunc)
        tc.save(s_kong, 'kong', oto_plosives_trunc)
        tc.save(s_kua, 'kua', oto_plosives)
        tc.save(s_kuo, 'kuo', oto_plosives)
        tc.save(s_kuai, 'kuai', oto_plosives_trunc)
        tc.save(s_kui, 'kui', oto_plosives_trunc)
        tc.save(s_kuan, 'kuan', oto_plosives_trunc)
        tc.save(s_kun, 'kun', oto_plosives_trunc)
        tc.save(s_kuang, 'kuang', oto_plosives_trunc)

    # === He ===

    c_h_filter = Pedalboard([
        Gain(-15),
        PeakFilter(1900, 7, 1900 / 1000),
        PeakFilter(5500, 5, 5500 / 3000),
        HighShelfFilter(8000, -50)
    ])
    c_h = c_h_filter(white_noise_base, sample_rate) * fricative_env

    if True:
        s_ha = vplos_cat(c_h, v_a)
        s_he = vplos_cat(c_h, v_e)
        s_hu = vplos_cat(c_h, v_u)
        s_hai = vplos_cat(c_h, vc_ai)
        s_hei = vplos_cat(c_h, vc_ei)
        s_hao = vplos_cat(c_h, vc_ao)
        s_hou = vplos_cat(c_h, vc_ou)
        s_han = vplos_cat(c_h, vc_an)
        s_hen = vplos_cat(c_h, vc_en)
        s_hang = vplos_cat(c_h, vc_ang)
        s_heng = vplos_cat(c_h, vc_eng)
        s_hong = vplos_cat(c_h, vc_ong)
        s_hua = clust_cat(c_h, vc_ua)
        s_huo = clust_cat(c_h, vc_uo)
        s_huai = clust_cat(c_h, vc_uai)
        s_hui = clust_cat(c_h, vc_uei)
        s_huan = clust_cat(c_h, vc_uan)
        s_hun = clust_cat(c_h, vc_uen)
        s_huang = clust_cat(c_h, vc_uang)

    if not skip_he:
        tc.save(c_h, 'h', oto_plosives_alone)
        tc.save(s_ha, 'ha', oto_plosives)
        tc.save(s_he, 'he', oto_plosives)
        tc.save(s_hu, 'hu', oto_plosives)
        tc.save(s_hai, 'hai', oto_plosives_trunc)
        tc.save(s_hei, 'hei', oto_plosives_trunc)
        tc.save(s_hao, 'hao', oto_plosives_trunc)
        tc.save(s_hou, 'hou', oto_plosives_trunc)
        tc.save(s_han, 'han', oto_plosives_trunc)
        tc.save(s_hen, 'hen', oto_plosives_trunc)
        tc.save(s_hang, 'hang', oto_plosives_trunc)
        tc.save(s_heng, 'heng', oto_plosives_trunc)
        tc.save(s_hong, 'hong', oto_plosives_trunc)
        tc.save(s_hua, 'hua', oto_plosives)
        tc.save(s_huo, 'huo', oto_plosives)
        tc.save(s_huai, 'huai', oto_plosives_trunc)
        tc.save(s_hui, 'hui', oto_plosives_trunc)
        tc.save(s_huan, 'huan', oto_plosives_trunc)
        tc.save(s_hun, 'hun', oto_plosives_trunc)
        tc.save(s_huang, 'huang', oto_plosives_trunc)

    # === Ji ===

    c_x_filter = Pedalboard([
        Gain(-1),
        PeakFilter(8000, 12, 8000 / 1500),
        LowShelfFilter(2500, -35),
        HighShelfFilter(11500, -40)
    ])
    c_j = c_x_filter(voiced_noise_base, sample_rate) * affricate_env

    if True:
        s_ji = vfrict_cat(c_j, v_i)
        s_ju = vfrict_cat(c_j, v_v)
        s_jue = vfrict_cat(c_j, vc_ve)
        s_jin = vfrict_cat(c_j, vc_in)
        s_jun = vfrict_cat(c_j, vc_vn)
        s_juan = vfrict_cat(c_j, vc_van)
        s_jing = vfrict_cat(c_j, vc_ing)
        s_jia = clust_cat(c_j, vc_ia)
        s_jie = clust_cat(c_j, vc_ie)
        s_jiao = clust_cat(c_j, vc_iao)
        s_jiu = clust_cat(c_j, vc_iou)
        s_jian = clust_cat(c_j, vc_ian)
        s_jiang = clust_cat(c_j, vc_iang)
        s_jiong = clust_cat(c_j, vc_iong)

    if not skip_ji:
        tc.save(c_j, 'j', oto_affricates_alone)
        tc.save(s_ji, 'ji', oto_affricates)
        tc.save(s_ju, 'ju', oto_affricates)
        tc.save(s_jue, 'jue', oto_affricates)
        tc.save(s_jin, 'jin', oto_affricates_trunc)
        tc.save(s_jun, 'jun', oto_affricates_trunc)
        tc.save(s_juan, 'juan', oto_affricates_trunc)
        tc.save(s_jing, 'jing', oto_affricates_trunc)
        tc.save(s_jia, 'jia', oto_affricates)
        tc.save(s_jie, 'jie', oto_affricates)
        tc.save(s_jiao, 'jiao', oto_affricates_trunc)
        tc.save(s_jiu, 'jiu', oto_affricates_trunc)
        tc.save(s_jian, 'jian', oto_affricates_trunc)
        tc.save(s_jiang, 'jiang', oto_affricates_trunc)
        tc.save(s_jiong, 'jiong', oto_affricates_trunc)

    # === Qi ===

    c_q = c_x_filter(white_noise_base, sample_rate) * affricate_env

    if True:
        s_qi = vfrict_cat(c_q, v_i)
        s_qu = vfrict_cat(c_q, v_v)
        s_que = vfrict_cat(c_q, vc_ve)
        s_qin = vfrict_cat(c_q, vc_in)
        s_qun = vfrict_cat(c_q, vc_vn)
        s_quan = vfrict_cat(c_q, vc_van)
        s_qing = vfrict_cat(c_q, vc_ing)
        s_qia = clust_cat(c_q, vc_ia)
        s_qie = clust_cat(c_q, vc_ie)
        s_qiao = clust_cat(c_q, vc_iao)
        s_qiu = clust_cat(c_q, vc_iou)
        s_qian = clust_cat(c_q, vc_ian)
        s_qiang = clust_cat(c_q, vc_iang)
        s_qiong = clust_cat(c_q, vc_iong)

    if not skip_qi:
        tc.save(c_q, 'q', oto_affricates_alone)
        tc.save(s_qi, 'qi', oto_affricates)
        tc.save(s_qu, 'qu', oto_affricates)
        tc.save(s_que, 'que', oto_affricates)
        tc.save(s_qin, 'qin', oto_affricates_trunc)
        tc.save(s_qun, 'qun', oto_affricates_trunc)
        tc.save(s_quan, 'quan', oto_affricates_trunc)
        tc.save(s_qing, 'qing', oto_affricates_trunc)
        tc.save(s_qia, 'qia', oto_affricates)
        tc.save(s_qie, 'qie', oto_affricates)
        tc.save(s_qiao, 'qiao', oto_affricates_trunc)
        tc.save(s_qiu, 'qiu', oto_affricates_trunc)
        tc.save(s_qian, 'qian', oto_affricates_trunc)
        tc.save(s_qiang, 'qiang', oto_affricates_trunc)
        tc.save(s_qiong, 'qiong', oto_affricates_trunc)

    # === Xi ===

    c_x = c_x_filter(white_noise_base, sample_rate) * fricative_env

    if True:
        s_xi = vfrict_cat(c_x, v_i)
        s_xu = vfrict_cat(c_x, v_v)
        s_xue = vfrict_cat(c_x, vc_ve)
        s_xin = vfrict_cat(c_x, vc_in)
        s_xun = vfrict_cat(c_x, vc_vn)
        s_xuan = vfrict_cat(c_x, vc_van)
        s_xing = vfrict_cat(c_x, vc_ing)
        s_xia = clust_cat(c_x, vc_ia)
        s_xie = clust_cat(c_x, vc_ie)
        s_xiao = clust_cat(c_x, vc_iao)
        s_xiu = clust_cat(c_x, vc_iou)
        s_xian = clust_cat(c_x, vc_ian)
        s_xiang = clust_cat(c_x, vc_iang)
        s_xiong = clust_cat(c_x, vc_iong)

    if not skip_xi:
        tc.save(c_x, 'x', oto_fricatives_alone)
        tc.save(s_xi, 'xi', oto_fricatives)
        tc.save(s_xu, 'xu', oto_fricatives)
        tc.save(s_xue, 'xue', oto_fricatives)
        tc.save(s_xin, 'xin', oto_fricatives_trunc)
        tc.save(s_xun, 'xun', oto_fricatives_trunc)
        tc.save(s_xuan, 'xuan', oto_fricatives_trunc)
        tc.save(s_xing, 'xing', oto_fricatives_trunc)
        tc.save(s_xia, 'xia', oto_fricatives)
        tc.save(s_xie, 'xie', oto_fricatives)
        tc.save(s_xiao, 'xiao', oto_fricatives_trunc)
        tc.save(s_xiu, 'xiu', oto_fricatives_trunc)
        tc.save(s_xian, 'xian', oto_fricatives_trunc)
        tc.save(s_xiang, 'xiang', oto_fricatives_trunc)
        tc.save(s_xiong, 'xiong', oto_fricatives_trunc)

    # === Zhi ===

    c_sh_filter = Pedalboard([
        Gain(-5),
        PeakFilter(2500, 15, 3000 / 1500),
        LowShelfFilter(1200, -35),
        HighShelfFilter(11000, -35)
    ])
    c_zh = c_sh_filter(voiced_noise_base, sample_rate) * affricate_env

    if True:
        s_zha = vfrict_cat(c_zh, v_a)
        s_zhe = vfrict_cat(c_zh, v_e)
        s_zhu = vfrict_cat(c_zh, v_u)
        s_zhi = vfrict_cat(c_zh, v_ir)
        s_zhai = vfrict_cat(c_zh, vc_ai)
        s_zhao = vfrict_cat(c_zh, vc_ao)
        s_zhou = vfrict_cat(c_zh, vc_ou)
        s_zhan = vfrict_cat(c_zh, vc_an)
        s_zhen = vfrict_cat(c_zh, vc_en)
        s_zhang = vfrict_cat(c_zh, vc_ang)
        s_zheng = vfrict_cat(c_zh, vc_eng)
        s_zhong = vfrict_cat(c_zh, vc_ong)
        s_zhua = clust_cat(c_zh, vc_ua)
        s_zhuo = clust_cat(c_zh, vc_uo)
        s_zhuai = clust_cat(c_zh, vc_uai)
        s_zhui = clust_cat(c_zh, vc_uei)
        s_zhuan = clust_cat(c_zh, vc_uan)
        s_zhun = clust_cat(c_zh, vc_uen)
        s_zhuang = clust_cat(c_zh, vc_uang)

    if not skip_zhi:
        tc.save(c_zh, 'zh', oto_affricates_alone)
        tc.save(s_zha, 'zha', oto_affricates)
        tc.save(s_zhe, 'zhe', oto_affricates)
        tc.save(s_zhu, 'zhu', oto_affricates)
        tc.save(s_zhi, 'zhi', oto_affricates)
        tc.save(s_zhai, 'zhai', oto_affricates_trunc)
        tc.save(s_zhao, 'zhao', oto_affricates_trunc)
        tc.save(s_zhou, 'zhou', oto_affricates_trunc)
        tc.save(s_zhan, 'zhan', oto_affricates_trunc)
        tc.save(s_zhen, 'zhen', oto_affricates_trunc)
        tc.save(s_zhang, 'zhang', oto_affricates_trunc)
        tc.save(s_zheng, 'zheng', oto_affricates_trunc)
        tc.save(s_zhong, 'zhong', oto_affricates_trunc)
        tc.save(s_zhua, 'zhua', oto_affricates)
        tc.save(s_zhuo, 'zhuo', oto_affricates)
        tc.save(s_zhuai, 'zhuai', oto_affricates_trunc)
        tc.save(s_zhui, 'zhui', oto_affricates_trunc)
        tc.save(s_zhuan, 'zhuan', oto_affricates_trunc)
        tc.save(s_zhun, 'zhun', oto_affricates_trunc)
        tc.save(s_zhuang, 'zhuang', oto_affricates_trunc)

    # === Chi ===

    c_ch = c_sh_filter(white_noise_base, sample_rate) * affricate_env

    if True:
        s_cha = vfrict_cat(c_ch, v_a)
        s_che = vfrict_cat(c_ch, v_e)
        s_chu = vfrict_cat(c_ch, v_u)
        s_chi = vfrict_cat(c_ch, v_ir)
        s_chai = vfrict_cat(c_ch, vc_ai)
        s_chao = vfrict_cat(c_ch, vc_ao)
        s_chou = vfrict_cat(c_ch, vc_ou)
        s_chan = vfrict_cat(c_ch, vc_an)
        s_chen = vfrict_cat(c_ch, vc_en)
        s_chang = vfrict_cat(c_ch, vc_ang)
        s_cheng = vfrict_cat(c_ch, vc_eng)
        s_chong = vfrict_cat(c_ch, vc_ong)
        s_chua = clust_cat(c_ch, vc_ua)
        s_chuo = clust_cat(c_ch, vc_uo)
        s_chuai = clust_cat(c_ch, vc_uai)
        s_chui = clust_cat(c_ch, vc_uei)
        s_chuan = clust_cat(c_ch, vc_uan)
        s_chun = clust_cat(c_ch, vc_uen)
        s_chuang = clust_cat(c_ch, vc_uang)

    if not skip_chi:
        tc.save(c_ch, 'ch', oto_affricates_alone)
        tc.save(s_cha, 'cha', oto_affricates)
        tc.save(s_che, 'che', oto_affricates)
        tc.save(s_chu, 'chu', oto_affricates)
        tc.save(s_chi, 'chi', oto_affricates)
        tc.save(s_chai, 'chai', oto_affricates_trunc)
        tc.save(s_chao, 'chao', oto_affricates_trunc)
        tc.save(s_chou, 'chou', oto_affricates_trunc)
        tc.save(s_chan, 'chan', oto_affricates_trunc)
        tc.save(s_chen, 'chen', oto_affricates_trunc)
        tc.save(s_chang, 'chang', oto_affricates_trunc)
        tc.save(s_cheng, 'cheng', oto_affricates_trunc)
        tc.save(s_chong, 'chong', oto_affricates_trunc)
        tc.save(s_chua, 'chua', oto_affricates)
        tc.save(s_chuo, 'chuo', oto_affricates)
        tc.save(s_chuai, 'chuai', oto_affricates_trunc)
        tc.save(s_chui, 'chui', oto_affricates_trunc)
        tc.save(s_chuan, 'chuan', oto_affricates_trunc)
        tc.save(s_chun, 'chun', oto_affricates_trunc)
        tc.save(s_chuang, 'chuang', oto_affricates_trunc)

    # === Shi ===

    c_sh = c_sh_filter(white_noise_base, sample_rate) * fricative_env

    if True:
        s_sha = vfrict_cat(c_sh, v_a)
        s_she = vfrict_cat(c_sh, v_e)
        s_shu = vfrict_cat(c_sh, v_u)
        s_shi = vfrict_cat(c_sh, v_ir)
        s_shai = vfrict_cat(c_sh, vc_ai)
        s_shao = vfrict_cat(c_sh, vc_ao)
        s_shou = vfrict_cat(c_sh, vc_ou)
        s_shan = vfrict_cat(c_sh, vc_an)
        s_shen = vfrict_cat(c_sh, vc_en)
        s_shang = vfrict_cat(c_sh, vc_ang)
        s_sheng = vfrict_cat(c_sh, vc_eng)
        s_shua = clust_cat(c_sh, vc_ua)
        s_shuo = clust_cat(c_sh, vc_uo)
        s_shuai = clust_cat(c_sh, vc_uai)
        s_shui = clust_cat(c_sh, vc_uei)
        s_shuan = clust_cat(c_sh, vc_uan)
        s_shun = clust_cat(c_sh, vc_uen)
        s_shuang = clust_cat(c_sh, vc_uang)

    if not skip_shi:
        tc.save(c_sh, 'sh', oto_fricatives_alone)
        tc.save(s_sha, 'sha', oto_fricatives)
        tc.save(s_she, 'she', oto_fricatives)
        tc.save(s_shu, 'shu', oto_fricatives)
        tc.save(s_shi, 'shi', oto_fricatives)
        tc.save(s_shai, 'shai', oto_fricatives_trunc)
        tc.save(s_shao, 'shao', oto_fricatives_trunc)
        tc.save(s_shou, 'shou', oto_fricatives_trunc)
        tc.save(s_shan, 'shan', oto_fricatives_trunc)
        tc.save(s_shen, 'shen', oto_fricatives_trunc)
        tc.save(s_shang, 'shang', oto_fricatives_trunc)
        tc.save(s_sheng, 'sheng', oto_fricatives_trunc)
        tc.save(s_shua, 'shua', oto_fricatives)
        tc.save(s_shuo, 'shuo', oto_fricatives)
        tc.save(s_shuai, 'shuai', oto_fricatives_trunc)
        tc.save(s_shui, 'shui', oto_fricatives_trunc)
        tc.save(s_shuan, 'shuan', oto_fricatives_trunc)
        tc.save(s_shun, 'shun', oto_fricatives_trunc)
        tc.save(s_shuang, 'shuang', oto_fricatives_trunc)

    # === Ri ===

    c_r = v_ir * fricative_env

    if True:
        s_re = vfrict_cat(c_r, v_e)
        s_ru = vfrict_cat(c_r, v_u)
        s_ri = vfrict_cat(c_r, v_ir)
        s_rao = vfrict_cat(c_r, vc_ao)
        s_rou = vfrict_cat(c_r, vc_ou)
        s_ran = vfrict_cat(c_r, vc_an)
        s_ren = vfrict_cat(c_r, vc_en)
        s_rang = vfrict_cat(c_r, vc_ang)
        s_reng = vfrict_cat(c_r, vc_eng)
        s_rong = vfrict_cat(c_r, vc_ong)
        s_rua = clust_cat(c_r, vc_ua)
        s_ruo = clust_cat(c_r, vc_uo)
        s_rui = clust_cat(c_r, vc_uei)
        s_ruan = clust_cat(c_r, vc_uan)
        s_run = clust_cat(c_r, vc_uen)

    if not skip_ri:
        tc.save(c_r, 'r', oto_fricatives_alone)
        tc.save(s_re, 're', oto_fricatives)
        tc.save(s_ru, 'ru', oto_fricatives)
        tc.save(s_ri, 'ri', oto_fricatives)
        tc.save(s_rao, 'rao', oto_fricatives_trunc)
        tc.save(s_rou, 'rou', oto_fricatives_trunc)
        tc.save(s_ran, 'ran', oto_fricatives_trunc)
        tc.save(s_ren, 'ren', oto_fricatives_trunc)
        tc.save(s_rang, 'rang', oto_fricatives_trunc)
        tc.save(s_reng, 'reng', oto_fricatives_trunc)
        tc.save(s_rong, 'rong', oto_fricatives_trunc)
        tc.save(s_rua, 'rua', oto_fricatives)
        tc.save(s_ruo, 'ruo', oto_fricatives)
        tc.save(s_rui, 'rui', oto_fricatives_trunc)
        tc.save(s_ruan, 'ruan', oto_fricatives_trunc)
        tc.save(s_run, 'run', oto_fricatives_trunc)

    # === Zi ===

    c_s_filter = Pedalboard([
        Gain(-5),
        PeakFilter(7200, 12, 7200 / 4500),
        LowShelfFilter(2250, -35),
        HighShelfFilter(11250, -45)
    ])
    c_z = c_s_filter(voiced_noise_base, sample_rate) * affricate_env

    if True:
        s_za = vfrict_cat(c_z, v_a)
        s_ze = vfrict_cat(c_z, v_e)
        s_zu = vfrict_cat(c_z, v_u)
        s_zi = vfrict_cat(c_z, v_iz)
        s_zai = vfrict_cat(c_z, vc_ai)
        s_zei = vfrict_cat(c_z, vc_ei)
        s_zao = vfrict_cat(c_z, vc_ao)
        s_zou = vfrict_cat(c_z, vc_ou)
        s_zan = vfrict_cat(c_z, vc_an)
        s_zen = vfrict_cat(c_z, vc_en)
        s_zang = vfrict_cat(c_z, vc_ang)
        s_zeng = vfrict_cat(c_z, vc_eng)
        s_zong = vfrict_cat(c_z, vc_ong)
        s_zuo = clust_cat(c_z, vc_uo)
        s_zui = clust_cat(c_z, vc_uei)
        s_zuan = clust_cat(c_z, vc_uan)
        s_zun = clust_cat(c_z, vc_uen)

    if not skip_zi:
        tc.save(c_z, 'z', oto_affricates_alone)
        tc.save(s_za, 'za', oto_affricates)
        tc.save(s_ze, 'ze', oto_affricates)
        tc.save(s_zu, 'zu', oto_affricates)
        tc.save(s_zi, 'zi', oto_affricates)
        tc.save(s_zai, 'zai', oto_affricates_trunc)
        tc.save(s_zei, 'zei', oto_affricates_trunc)
        tc.save(s_zao, 'zao', oto_affricates_trunc)
        tc.save(s_zou, 'zou', oto_affricates_trunc)
        tc.save(s_zan, 'zan', oto_affricates_trunc)
        tc.save(s_zen, 'zen', oto_affricates_trunc)
        tc.save(s_zang, 'zang', oto_affricates_trunc)
        tc.save(s_zeng, 'zeng', oto_affricates_trunc)
        tc.save(s_zong, 'zong', oto_affricates_trunc)
        tc.save(s_zuo, 'zuo', oto_affricates)
        tc.save(s_zui, 'zui', oto_affricates_trunc)
        tc.save(s_zuan, 'zuan', oto_affricates_trunc)
        tc.save(s_zun, 'zun', oto_affricates_trunc)

    # === Ci ===

    c_c = c_s_filter(white_noise_base, sample_rate) * affricate_env

    if True:
        s_ca = vfrict_cat(c_c, v_a)
        s_ce = vfrict_cat(c_c, v_e)
        s_cu = vfrict_cat(c_c, v_u)
        s_ci = vfrict_cat(c_c, v_iz)
        s_cai = vfrict_cat(c_c, vc_ai)
        s_cao = vfrict_cat(c_c, vc_ao)
        s_cou = vfrict_cat(c_c, vc_ou)
        s_can = vfrict_cat(c_c, vc_an)
        s_cen = vfrict_cat(c_c, vc_en)
        s_cang = vfrict_cat(c_c, vc_ang)
        s_ceng = vfrict_cat(c_c, vc_eng)
        s_cong = vfrict_cat(c_c, vc_ong)
        s_cuo = clust_cat(c_c, vc_uo)
        s_cui = clust_cat(c_c, vc_uei)
        s_cuan = clust_cat(c_c, vc_uan)
        s_cun = clust_cat(c_c, vc_uen)

    if not skip_ci:
        tc.save(c_c, 'c', oto_affricates_alone)
        tc.save(s_ca, 'ca', oto_affricates)
        tc.save(s_ce, 'ce', oto_affricates)
        tc.save(s_cu, 'cu', oto_affricates)
        tc.save(s_ci, 'ci', oto_affricates)
        tc.save(s_cai, 'cai', oto_affricates_trunc)
        tc.save(s_cao, 'cao', oto_affricates_trunc)
        tc.save(s_cou, 'cou', oto_affricates_trunc)
        tc.save(s_can, 'can', oto_affricates_trunc)
        tc.save(s_cen, 'cen', oto_affricates_trunc)
        tc.save(s_cang, 'cang', oto_affricates_trunc)
        tc.save(s_ceng, 'ceng', oto_affricates_trunc)
        tc.save(s_cong, 'cong', oto_affricates_trunc)
        tc.save(s_cuo, 'cuo', oto_affricates)
        tc.save(s_cui, 'cui', oto_affricates_trunc)
        tc.save(s_cuan, 'cuan', oto_affricates_trunc)
        tc.save(s_cun, 'cun', oto_affricates_trunc)

    # === Si ===

    c_s = c_s_filter(white_noise_base, sample_rate) * fricative_env

    if True:
        s_sa = vfrict_cat(c_s, v_a)
        s_se = vfrict_cat(c_s, v_e)
        s_su = vfrict_cat(c_s, v_u)
        s_si = vfrict_cat(c_s, v_iz)
        s_sai = vfrict_cat(c_s, vc_ai)
        s_sao = vfrict_cat(c_s, vc_ao)
        s_sou = vfrict_cat(c_s, vc_ou)
        s_san = vfrict_cat(c_s, vc_an)
        s_sen = vfrict_cat(c_s, vc_en)
        s_sang = vfrict_cat(c_s, vc_ang)
        s_seng = vfrict_cat(c_s, vc_eng)
        s_song = vfrict_cat(c_s, vc_ong)
        s_suo = clust_cat(c_s, vc_uo)
        s_sui = clust_cat(c_s, vc_uei)
        s_suan = clust_cat(c_s, vc_uan)
        s_sun = clust_cat(c_s, vc_uen)

    if not skip_si:
        tc.save(c_s, 's', oto_affricates_alone)
        tc.save(s_sa, 'sa', oto_affricates)
        tc.save(s_se, 'se', oto_affricates)
        tc.save(s_su, 'su', oto_affricates)
        tc.save(s_si, 'si', oto_affricates)
        tc.save(s_sai, 'sai', oto_affricates_trunc)
        tc.save(s_sao, 'sao', oto_affricates_trunc)
        tc.save(s_sou, 'sou', oto_affricates_trunc)
        tc.save(s_san, 'san', oto_affricates_trunc)
        tc.save(s_sen, 'sen', oto_affricates_trunc)
        tc.save(s_sang, 'sang', oto_affricates_trunc)
        tc.save(s_seng, 'seng', oto_affricates_trunc)
        tc.save(s_song, 'song', oto_affricates_trunc)
        tc.save(s_suo, 'suo', oto_affricates)
        tc.save(s_sui, 'sui', oto_affricates_trunc)
        tc.save(s_suan, 'suan', oto_affricates_trunc)
        tc.save(s_sun, 'sun', oto_affricates_trunc)

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

    print(f'[Info] {tc.save_count} files saved/overwritten successfully.')

    tc.save_oto()

    config = {
        'text_file_encoding': 'utf-8',
        'name': 'Technebit β1.0 Zh-CVV',
        'localized_names': {
            'ja-JP': 'テクネビット β1.0 中国語-CVV',
            'zh-CN': '锝比特 β1.0 汉语-CVV',
            'zh-TW': '鍀比特 β1.0 漢語-CVV'
        },
        'author': 'Generated soundbank - Python program by Nomani',
        'voice': 'FM Synthesizer (literally)',
        'version': 'β1.0',
        'web': 'https://github.com/path/to/project',
        'image': {
            'base': 'image_beta_zh_cvv_b1.0.png',
            'overlay': {
                'text': 'Tcb Zh-CVV\nb1.0',
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
                'text': 'Technebit Zh-CVV b1.0\nGen time {t}\n{s}',
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