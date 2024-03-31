import re

replace_words = {
    r"\bG'": "Ğ",
    r"\bg'": "ğ",
    r"\bO'": "Ŏ",
    r"\bo'": "ŏ",
    r".G'\b": ".Ğ",
    r".O'\b": ".Ŏ",
    r"G'.": "Ğ.",
    r"O'.": "Ŏ.",

    "Rŏbaro'": "Rŏbarŏ",
    "rŏbaro'": "rŏbarŏ",

    "Rŏparo'": "Rŏparŏ",
    "rŏparo'": "rŏparŏ",

    "Rubaro'": "Rubarŏ",
    "rubaro'": "rubarŏ",

    "Obro'": "Obrŏ",
    "obro'": "obrŏ",

    "Beobro'": "Beobrŏ",
    "beobro'": "beobrŏ",

    r"\bSo'": "Sŏ",
    r"\bso'": "sŏ",

    "Gulro'": "Gulrŏ",
    "gulro'": "gulrŏ",

    "Ijmo'": "Ijmŏ",
    "ijmo'": "ijmŏ",

    "Yo'": "Yŏ",
    "yo'": "yŏ",

    "Bio'": "Biŏ",
    "bio'": "biŏ",

    "Peshko'": "Peshkŏ",
    "Borshitao'": "Borshitaŏ",
    "Ebro'": "Ebrŏ",
    "Qarnoqcho'": "Qarnoqchŏ",
    "Eroglo'": "Eroglŏ",
    "Beyneo'": "Beyneŏ",
    "Toktao'": "Toktaŏ",
    "Woy-Wo'": "Woy-Wŏ",
    "Aqro'": "Aqrŏ",

    "Voy-bo'!": "Voy-bŏ!",
    "Ŏh-ho'!": "Ŏh-hŏ!",
    "ŏx-xo'!": "ŏx-xŏ!",
    "hŏo'": "hŏŏ",
    "lil-amo'": "lil-amŏ",
    "ŎTIBDO'": "ŎTIBDŎ",

    "RO'": "RŎ",
    "TRO'": "TRŎ",
    "RAO'": "RAŎ",
    "IFO'": "IFŎ",

    "Chog'": "Choğ",
    "chog'": "choğ",

    "Mablag'": "Mablağ",
    "mablag'": "mablağ",

    "Yarog'": "Yaroğ",
    "yarog'": "yaroğ",

    "Qutlug'": "Qutluğ",
    "qutlug'": "qutluğ",

    "Urug'": "Uruğ",
    "urug'": "uruğ",

    "Bog'": "Boğ",
    "bog'": "boğ",
    "BOG'": "BOĞ",

    "Tog'": "Toğ",
    "tog'": "toğ",

    "Yog'": "Yoğ",
    "yog'": "yoğ",

    "Sog'": "Soğ",
    "sog'": "soğ",

    "Dog'": "Doğ",
    "dog'": "doğ",

    "Yorug'": "Yoruğ",
    "yorug'": "yoruğ",

    "Ulug'": "Uluğ",
    "ulug'": "uluğ",

    "Yorog'": "Yoroğ",
    "yorog'": "yoroğ",

    "Yanglig'": "Yangliğ",
    "yanglig'": "yangliğ",

    "Chŏg'": "Chŏğ",
    "chŏg'": "chŏğ",

    "Tig'": "Tiğ",
    "tig'": "tiğ",

    "Forig'": "Foriğ",
    "forig'": "foriğ",

    "Bug'": "Buğ",
    "bug'": "buğ",

    "Jag'": "Jağ",
    "jag'": "jağ",

    "Dimog'": "Dimoğ",
    "dimog'": "dimoğ",

    "Dovrug'": "Dovruğ",
    "dovrug'": "dovruğ",

    "Yig'": "Yiğ",
    "yig'": "yiğ",

    "Zog'": "Zoğ",
    "zog'": "zoğ",

    "Darig'": "Dariğ",
    "darig'": "dariğ",

    "Rog'": "Roğ",
    "rog'": "roğ",

    "Tug'": "Tuğ",
    "tug'": "tuğ",

    "Otlig'": "Otliğ",
    "otlig'": "otliğ",

    "Semurg'": "Semurğ",
    "semurg'": "semurğ",

    "Qovug'": "Qovuğ",
    "qovug'": "qovuğ",

    "Kutlug'": "Kutluğ",
    "kutlug'": "kutluğ",

    "Hoqonlig'": "Hoqonliğ",
    "hoqonlig'": "hoqonliğ",

    "Arqadag'": "Arqadağ",
    "arqadag'": "arqadağ",
    "arkadag'": "arkadağ",

    "Bŏzdog'": "Bŏzdoğ",
    "Qorabog'": "Qoraboğ",
    "Gulbog'": "Gulboğ",
    "Abdusamig'": "Abdusamiğ",
    "al-Marug'": "al-Maruğ",
    "Arkadag'": "Arkadağ",
    "Qorabag'": "Qorabağ",
    "Saneg'": "Saneğ",
    "Qilichdorŏg'": "Qilichdorŏğ",
    "Dushanbe-Kŏlob-Xorŏg'": "Dushanbe-Kŏlob-Xorŏğ",
    "Bŏzdag'": "Bŏzdağ",
    "Ŏzdag'": "Ŏzdağ",
    "Bertug'": "Bertuğ",
    "Yanardag'": "Yanardağ",
    "Bozdag'": "Bozdağ",
    "Tekirdag'": "Tekirdağ",
    "Quğlug'": "Quğluğ",
    "Akchag'": "Akchağ",
    "Oqchog'": "Oqchoğ",
    "Juzimbag'": "Juzimbağ",
    "Xorug'": "Xoruğ",
    "Horug'": "Horuğ",
    "Poytug'": "Poytuğ",
    "Ertug'": "Ertuğ",
    "Uludag'": "Uludağ",
    "POYTUG'": "POYTUĞ",
    "Elyazig'": "Elyaziğ",
    "Vozig'": "Voziğ",
    "Samandag'": "Samandağ",

    "YoG'": "YoĞ",
}


def custom_replace(s: str) -> str:
    s = s.replace("G'", "Ğ")
    s = s.replace("g'", "ğ")
    s = s.replace("O'", "Ŏ")
    s = s.replace("o'", "ŏ")
    match = re.search(r"[ĞğŎŏ]s?\W", s)
    while match:
        old = match.group()
        new = old.replace("Ğ", "G'")
        new = new.replace("ğ", "g'")
        new = new.replace("Ŏ", "O'")
        new = new.replace("ŏ", "o'")
        s = s.replace(old, new)
        match = re.search(r"[ĞğŎŏ]s?\W", s)
    for old, new in replace_words.items():
        s = re.sub(old, new, s)
    return s
