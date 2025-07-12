from dataclasses import dataclass, asdict
from lexical import (
    asciify,
    count_nasal_phonemes,
    count_r_pronounciations,
    count_sharp_phonemes,
    is_vowel,
    split_syllables,
)


from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Featured:
    original: str
    syllables: List[str]
    ends_in_vowel: bool
    ending_vowel: Optional[str]
    ending_consonant: Optional[str]
    nasal_count: int
    sharp_count: int
    a_count: int
    i_count: int
    u_count: int
    e_count: int
    o_count: int
    rome_r_count: int
    potato_r_count: int
    laughed_r_count: int
    gender: str

    @staticmethod
    def from_row(word: str, gender: str) -> "Featured":
        syllables = split_syllables(word)

        word = asciify(word)

        ends_in_vowel = is_vowel(word[-1])

        if ends_in_vowel:
            ending_vowel = word[-1]
            ending_consonant = None
        else:
            ending_consonant = word[-1]
            ending_vowel = next((c for c in syllables[-1][::-1] if is_vowel(c)), None)

        nasal_count = count_nasal_phonemes(word)
        sharp_count = count_sharp_phonemes(word)

        lower = word.lower()
        a_count = lower.count("a")
        i_count = lower.count("i")
        u_count = lower.count("u")
        e_count = lower.count("e")
        o_count = lower.count("o")

        rome_r, potato_r, laughed_r = count_r_pronounciations(word)

        return Featured(
            original=word,
            syllables=syllables,
            ends_in_vowel=ends_in_vowel,
            ending_vowel=ending_vowel,
            ending_consonant=ending_consonant,
            nasal_count=nasal_count,
            sharp_count=sharp_count,
            a_count=a_count,
            i_count=i_count,
            u_count=u_count,
            e_count=e_count,
            o_count=o_count,
            rome_r_count=rome_r,
            potato_r_count=potato_r,
            laughed_r_count=laughed_r,
            gender=gender,
        )

