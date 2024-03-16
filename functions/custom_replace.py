import re

replace_words = {
    " G'": " Ǧ",
    " g'": " ǧ",
    " O'": " Õ",
    " o'": " õ",
    ".G' ": ".Ǧ ",
    ".O' ": ".Õ ",
    "G'.": "Ǧ.",
    "O'.": "Õ.",

    "Rõbaro'": "Rõbarõ",
    "rõbaro'": "rõbarõ",

    "Obro'": "Obrõ",
    "obro'": "obrõ",

    "Beobro'": "Beobrõ",
    "beobro'": "beobrõ",

    "Peshko'": "Peshkõ",
    "Borshitao'": "Borshitaõ",
    "Ebro'": "Ebrõ",
    "RO'": "RÕ",
    "TRO'": "TRÕ",

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
    "BOG'": "BOǦ",

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

    "Darig'": "Dariǧ",
    "darig'": "dariǧ",

    "Rog'": "Roǧ",
    "rog'": "roǧ",

    "Tug'": "Tuǧ",
    "tug'": "tuǧ",

    "Arqadag'": "Arqadaǧ",
    "arqadag'": "arqadaǧ",
    "arkadag'": "arkadaǧ",

    "Bõzdog'": "Bõzdoǧ",
    "Qorabog'": "Qoraboǧ",
    "Gulbog'": "Gulboǧ",
    "Abdusamig'": "Abdusamiǧ",
    "al-Marug'": "al-Maruǧ",
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
    "Akchag'": "Akchaǧ",
    "Oqchog'": "Oqchoǧ",
    "Juzimbag'": "Juzimbaǧ",
    "Xorug'": "Xoruǧ",
    "Horug'": "Horuǧ",
    "Poytug'": "Poytuǧ",
    "Ertug'": "Ertuǧ",
}


def custom_replace(s: str) -> str:
    s = s.replace("G'", "Ǧ")
    s = s.replace("g'", "ǧ")
    s = s.replace("O'", "Õ")
    s = s.replace("o'", "õ")
    match = re.search(r"[ǦǧÕõ]s?\W", s)
    while match:
        old = match.group(0)
        new = old.replace("Ǧ", "G'")
        new = new.replace("ǧ", "g'")
        new = new.replace("Õ", "O'")
        new = new.replace("õ", "o'")
        s = s.replace(old, new)
        match = re.search(r"[ǦǧÕõ]s?\W", s)
    for old, new in replace_words.items():
        s = s.replace(old, new)
    return s
