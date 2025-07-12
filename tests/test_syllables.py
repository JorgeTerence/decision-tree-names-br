import pytest
from lib.lexical import split_syllables


@pytest.mark.parametrize(
    "word, expected",
    [
        ("abaco", ["a", "ba", "co"]),
        ("cavalo", ["ca", "va", "lo"]),
        ("gaveta", ["ga", "ve", "ta"]),
        ("fone", ["fo", "ne"]),
        ("pirata", ["pi", "ra", "ta"]),
        ("vaso", ["va", "so"]),
    ],
)
def test_hard_breaks(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("teclado", ["te", "cla", "do"]),
        ("fraco", ["fra", "co"]),
        ("grama", ["gra", "ma"]),
        ("plano", ["pla", "no"]),
        ("bravo", ["bra", "vo"]),
        ("trapo", ["tra", "po"]),
        ("primata", ["pri", "ma", "ta"]),
    ],
)
def test_lr_compound_breaks(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("porta", ["por", "ta"]),
        ("marmita", ["mar", "mi", "ta"]),
        ("fartura", ["far", "tu", "ra"]),
        ("marco", ["mar", "co"]),
        ("garfo", ["gar", "fo"]),
        ("gordo", ["gor", "do"]),
        ("festa", ["fes", "ta"]),
        ("mistura", ["mis", "tu", "ra"]),
        ("espanto", ["es", "pan", "to"]),
        ("pampa", ["pam", "pa"]),
    ],
)
def test_half_bounce_break(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("livros", ["li", "vros"]),
        ("fracos", ["fra", "cos"]),
        ("portas", ["por", "tas"]),
        ("ramal", ["ra", "mal"]),
        ("gatil", ["ga", "til"]),
        ("mortos", ["mor", "tos"]),
        ("asmatico", ["as", "ma", "ti", "co"]),
    ],
)
def test_consonant_endings(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("asas", ["a", "sas"]),
        ("fusao", ["fu", "sao"]),
        ("mizu", ["mi", "zu"]),
        ("musa", ["mu", "sa"]),
    ],
)
def test_sz_break(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [("assado", ["as", "sa", "do"]), ("passada", ["pas", "sa", "da"])],
)
def test_double_s(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("falhou", ["fa", "lhou"]),
        ("manha", ["ma", "nha"]),
        ("malha", ["ma", "lha"]),
        ("minha", ["mi", "nha"]),
        ("bicho", ["bi", "cho"]),
        ("mulher", ["mu", "lher"]),
    ],
)
def test_h_compound(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("balaio", ["ba", "lai", "o"]),
        ("melancia", ["me", "lan", "ci", "a"]),
    ],
)
def test_double_vowel_break(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("ana", ["a", "na"]),
        ("guilherme", ["gui", "lher", "me"]),
        ("larica", ["la", "ri", "ca"]),
        ("marina", ["ma", "ri", "na"]),
        ("nicolau", ["ni", "co", "lau"]),
        ("nicolas", ["ni", "co", "las"]),
        ("virginia", ["vir", "gi", "ni", "a"]),
        ("jorge", ["jor", "ge"]),
        ("zacarias", ["za", "ca", "ri", "as"]),
        ("rafael", ["ra", "fa", "el"]),
    ],
)
def test_names(word, expected):
    assert split_syllables(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("esfiha", ["es", "fi", "ha"]),
        ("raphael", ["ra", "pha", "el"]),
        ("murro", ["mur", "ro"]),
        ("porrada", ["por", "ra", "da"]),
        ("homem", ["ho", "mem"]),
        ("capacete", ["ca", "pa", "ce", "te"]),
        ("ceda", ["ce", "da"]),
    ],
)
def test_edge_cases(word, expected):
    assert split_syllables(word) == expected
