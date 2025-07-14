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
from typing import Any, Hashable, Optional, List


@dataclass
class Featured:
    # original: str
    syllables: List[str]
    normalized_syllables: List[str]

    ends_in_vowel: bool
    ending_vowel: Optional[str]
    ending_consonant: Optional[str]

    starts_in_vowel: bool
    starting_vowel: str
    starting_consonant: Optional[str]

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

    s_count: int

    gender: str

    @staticmethod
    def from_row(row: dict[Hashable, Any]) -> "Featured":
        _name = asciify(row["name"])
        syllables = split_syllables(_name)

        ends_in_vowel = is_vowel(_name[-1])

        if ends_in_vowel:
            ending_vowel = _name[-1]
            ending_consonant = None
        else:
            ending_consonant = _name[-1]
            ending_vowel = next((c for c in syllables[-1][::-1] if is_vowel(c)), None)

        starts_in_vowel = is_vowel(_name[0])

        if starts_in_vowel:
            starting_vowel = _name[0]
            starting_consonant = None
        else:
            starting_consonant = _name[0]
            try:
                starting_vowel = [char for char in syllables[0] if is_vowel(char)][0]
            except Exception as e:
                print(syllables)
                raise e

        rome_r, potato_r, laughed_r = count_r_pronounciations(_name)

        return Featured(
            # original=row["name"],
            syllables=syllables,
            normalized_syllables=split_syllables(_name),
            ends_in_vowel=ends_in_vowel,
            ending_vowel=ending_vowel,
            ending_consonant=ending_consonant,
            nasal_count=count_nasal_phonemes(_name),
            sharp_count=count_sharp_phonemes(_name),
            a_count=_name.count("a"),
            i_count=_name.count("i"),
            u_count=_name.count("u"),
            e_count=_name.count("e"),
            o_count=_name.count("o"),
            rome_r_count=rome_r,
            potato_r_count=potato_r,
            laughed_r_count=laughed_r,
            starts_in_vowel=starts_in_vowel,
            starting_vowel=starting_vowel,
            starting_consonant=starting_consonant,
            s_count=_name.count("ss")
            + _name.count("ce")
            + _name.count("ci")
            + row["name"].count("ç")
            + _name.startswith("s"),
            gender=row["gender"],
        )
