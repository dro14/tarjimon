import re

replace_words = {
    "Rõbaro'": "Rõbarõ",
    "rõbaro'": "rõbarõ",

    "Obro'": "Obrõ",
    "obro'": "obrõ",

    "Beobro'": "Beobrõ",
    "beobro'": "beobrõ",

    "Peshko'": "Peshkõ",

    "Voy-bo'!": "Voy-bõ!",

    "Õh-ho'!": "Õh-hõ!",

    "Chog'": "Choǧ",
    "chog'": "choǧ",

    "Mablag'": "Mablaǧ",
    "mablag'": "mablaǧ",

    "Yarog'": "Yaroǧ",
    "yarog'": "yaroǧ",

    "Qutlug'": "Qutluǧ",
    "qutlug'": "qutluǧ",

    "Urug'": "Uruǧ",
    "urug'": "uruǧ",

    "Bog'": "Boǧ",
    "bog'": "boǧ",

    "Tog'": "Toǧ",
    "tog'": "toǧ",

    "Yog'": "Yoǧ",
    "yog'": "yoǧ",

    "Sog'": "Soǧ",
    "sog'": "soǧ",

    "Dog'": "Doǧ",
    "dog'": "doǧ",

    "Yorug'": "Yoruǧ",
    "yorug'": "yoruǧ",

    "Ulug'": "Uluǧ",
    "ulug'": "uluǧ",

    "Yorog'": "Yoroǧ",
    "yorog'": "yoroǧ",

    "Yanglig'": "Yangliǧ",
    "yanglig'": "yangliǧ",

    "Chõg'": "Chõǧ",
    "chõg'": "chõǧ",

    "Tig'": "Tiǧ",
    "tig'": "tiǧ",

    "Forig'": "Foriǧ",
    "forig'": "foriǧ",

    "Bug'": "Buǧ",
    "bug'": "buǧ",

    "Jag'": "Jaǧ",
    "jag'": "jaǧ",

    "Dimog'": "Dimoǧ",
    "dimog'": "dimoǧ",

    "Dovrug'": "Dovruǧ",
    "dovrug'": "dovruǧ",

    "Yig'": "Yiǧ",
    "yig'": "yiǧ",

    "Zog'": "Zoǧ",
    "zog'": "zoǧ",

    "G'.": "Ǧ.",
    "Bõzdog'": "Bõzdoǧ",
    "Qorabog'": "Qoraboǧ",
    "Gulbog'": "Gulboǧ",
    "Abdusamig'": "Abdusamiǧ",
    "al-Marug'": "al-Maruǧ",
    "Arqadag'": "Arqadaǧ",
    "Arkadag'": "Arkadaǧ",
    "Semurg'": "Semurǧ",
    "Qorabag'": "Qorabaǧ",
    "Saneg'": "Saneǧ",
    "Qilichdorõg'": "Qilichdorõǧ",
    "Dushanbe-Kõlob-Xorõg'": "Dushanbe-Kõlob-Xorõǧ",
    "Bõzdag'": "Bõzdaǧ",
    "Õzdag'": "Õzdaǧ",
    "Bertug'": "Bertuǧ",
    "Yanardag'": "Yanardaǧ",
    "Bozdag'": "Bozdaǧ",
    "Tekirdag'": "Tekirdaǧ",
    "Quǧlug'": "Quǧluǧ",
}


def preprocess(s):
    s = s.replace("G'", "Ǧ")
    s = s.replace("g'", "ǧ")
    s = s.replace("O'", "Õ")
    s = s.replace("o'", "õ")
    match = re.search(r"[ǦǧÕõ]s?[\s\",;:.!?)}\]]", s)
    while match:
        old = match.group(0)
        new = old.replace("Ǧ", "G'")
        new = new.replace("ǧ", "g'")
        new = new.replace("Õ", "O'")
        new = new.replace("õ", "o'")
        s = s.replace(old, new)
        match = re.search(r"[ǦǧÕõ]s?[\s\",;:.!?)}\]]", s)
    for old, new in replace_words.items():
        s = s.replace(old, new)
    return s
