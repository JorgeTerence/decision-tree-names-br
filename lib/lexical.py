import unicodedata

VOWELS = ["a", "i", "u", "e", "o", "y"]
SKIPPABLE = ["l", "r", "s", "m", "n", "h"]

NASAL_CONSONANTS = ["z", "d", "v", "g", "b"]
SHARP_CONSONANTS = ["q", "k", "t", "p"]

is_vowel = lambda c: c in VOWELS
is_consonant = lambda c: c not in VOWELS
is_nasal = lambda c: c in NASAL_CONSONANTS
is_sharp = lambda c: c in SHARP_CONSONANTS


def asciify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(c for c in normalized if not unicodedata.combining(c)).lower()


def char_slide(s):
    return list(zip([None] + list(s), s, list(s[1:]) + [None]))


def split_syllables(word: str) -> list[str]:
    breakpoints = []
    current = ""

    for i, (prev_char, char, next_char) in enumerate(char_slide(asciify(word))):
        if (
            is_consonant(char)
            and current != ""
            and (
                char not in SKIPPABLE  # compound break
                or is_vowel(prev_char)
                or prev_char in SKIPPABLE  # mar-mi-ta
                and char != "h"
            )
            # bounce break
            and not (char in SKIPPABLE and is_consonant(next_char) and next_char != "h")
        ):
            breakpoints.append(i)
            current = ""

        if char == "i" and is_vowel(next_char):
            breakpoints.append(i + 1)
            current = ""
            continue

        if char == "a" and next_char == "e":
            breakpoints.append(i + 1)
            current = ""
            continue

        current += char

    breakpoints.append(i + 1)
    return [word[a:b] for a, b in zip([0] + breakpoints, breakpoints)]


def count_nasal_phonemes(word: str) -> int:
    nasal_s_occurrences = 0

    # check where does 's' behave like 'z'
    for prev_char, char, next_char in char_slide(word):
        if char == "s" and is_vowel(prev_char) and is_vowel(next_char):
            nasal_s_occurrences += 1

    return sum(is_nasal(c) for c in word) + nasal_s_occurrences


def count_sharp_phonemes(word: str) -> int:
    sharp_c_occurrences = 0

    # check where does 'c' behave like 'k'
    for _, char, next_char in char_slide(word):
        if char == "c" and next_char not in ["i", "e"]:
            sharp_c_occurrences += 1

    return sum(is_sharp(c) for c in word) + sharp_c_occurrences


def count_r_pronounciations(word: str) -> tuple[int, int, int]:
    rome_count = 0
    potato_count = 0

    for _, char, next_char in char_slide(word)[1:]:
        if char == "r":
            if is_vowel(next_char):
                rome_count += 1
            else:
                potato_count += 1

    return (
        rome_count,  # rome
        potato_count,  # potato
        word.count("rr") + word.startswith("r"),  # laughed
    )
