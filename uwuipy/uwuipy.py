from __future__ import annotations

import re
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union

import unicodedata


URI_REGEX = r"(?:[a-zA-Z]+:)+/*(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"


class Uwuipy:
    """
    :param power: an integer from 1 to 4 that controls how strong uwuification is. (the exact transformations applied are in :py:attr:`__uwu_patterns`)
    """

    # Uwuification level = index + 1
    __uwu_patterns: list[list[tuple[str, str]]] = [
        [
            (r"[rl]", r"w"),
            (r"[RL]", r"W"),
        ],
        [
            (r"([nj])([aeiou])", r"\g<1>y\g<2>"),
            (r"([NJ])([aeiou])", r"\g<1>y\g<2>"),
            (r"([NJ])([AEIOU])", r"\g<1>Y\g<2>"),
        ],
        [
            (r"ove", r"uv"),
            (r"v([aeiouAEIUO])", r"w\g<1>"),
        ],
        [
            (r"ose", r"owse"),
            (r"([Oo])h", r"\g<1>wh"),
            (r"([Oo])n", r"\g<1>wn"),
            (r"([Aa])n", r"\g<1>wn"),
        ],
    ]

    __actions = [
        "***blushes***",
        "***whispers to self***",
        "***cries***",
        "***screams***",
        "***sweats***",
        "***runs away***",
        "***screeches***",
        "***walks away***",
        "***looks at you***",
        "***huggles tightly***",
        "***boops your nose***",
        "***wags my tail***",
        "***pounces on you***",
        "***nuzzles your necky wecky***",
        "***licks lips***",
        "***glomps and huggles***",
        "***glomps***",
        "***looks around suspiciously***",
        "***smirks smugly***",
    ]

    # Because Kazani got annoyed at not being able to disable them.
    __nsfw_actions = [
        "***twerks***",  # arguably nsfw
        "***sees bulge***",
        "***notices buldge***",
        "***starts twerking***",  # also arguable.
        "***unzips your pants***",
        "***pounces on your buldge***",
    ]

    __exclamations = {
        "!": [
            "!",
            "!!",
            "!!!",
            "!!11",
            "!!1!",
        ],
        "?": [
            "?",
            "??",
            "???",
            "!?",
            "?!!",
            "?!?1",
            "?!?!",
        ],
    }

    __faces = [
        r"(・\`ω\´・)",
        ";;w;;",
        "OwO",
        "owo",
        "UwU",
        r"\>w\<",
        "^w^",
        "ÚwÚ",
        "^-^",
        ":3",
        "x3",
        "Uwu",
        "uwU",
        "(uwu)",
        "(ᵘʷᵘ)",
        "(ᵘﻌᵘ)",
        "(◡ ω ◡)",
        "(◡ ꒳ ◡)",
        "(◡ w ◡)",
        "(◡ ሠ ◡)",
        "(˘ω˘)",
        "(⑅˘꒳˘)",
        "(˘ᵕ˘)",
        "(˘ሠ˘)",
        "(˘³˘)",
        "(˘ε˘)",
        "(˘˘˘)",
        "( ᴜ ω ᴜ )",
        "(„ᵕᴗᵕ„)",
        "(ㅅꈍ ˘ ꈍ)",
        "(⑅˘꒳˘)",
        "( ｡ᵘ ᵕ ᵘ ｡)",
        "( ᵘ ꒳ ᵘ ✼)",
        "( ˘ᴗ˘ )",
        "(ᵕᴗ ᵕ⁎)",
        "*:･ﾟ✧(ꈍᴗꈍ)✧･ﾟ:*",
        "*˚*(ꈍ ω ꈍ).₊̣̇.",
        "(。U ω U。)",
        "(U ᵕ U❁)",
        "(U ﹏ U)",
        "(◦ᵕ ˘ ᵕ◦)",
        "ღ(U꒳Uღ)",
        "♥(。U ω U。)",
        "– ̗̀ (ᵕ꒳ᵕ) ̖́-",
        "( ͡U ω ͡U )",
        "( ͡o ᵕ ͡o )",
        "( ͡o ꒳ ͡o )",
        "( ˊ.ᴗˋ )",
        "(ᴜ‿ᴜ✿)",
        "~(˘▾˘~)",
        "(｡ᴜ‿‿ᴜ｡)",
        ">/////<",
    ]

    def __init__(
        self,
        seed: Union[int, None] = None,
        stutter_chance: float = 0.1,
        face_chance: float = 0.05,
        action_chance: float = 0.075,
        exclamation_chance: float = 1,
        nsfw_actions: bool = False,
        power: int = 3,  # 4 is a little too much to make the default.
    ):
        # input protection to make sure the user stays within allowed parameters

        for name in [
            "stutter_chance",
            "face_chance",
            "action_chance",
            "exclamation_chance",
        ]:
            if not 0.0 <= locals()[name] <= 1.0:
                raise ValueError(
                    f"`{name}` must be a float between 0.0 and 1.0 (inclusive)"
                )

        if not 1 <= power <= 4:
            raise ValueError("`power` must be between 1 and 4 (inclusive)")

        random.seed(seed)
        self._uwu_patterns = self.__uwu_patterns[0]

        for level in range(1, power):
            self._uwu_patterns.extend(self.__uwu_patterns[level])

        self._stutter_chance = stutter_chance
        self._face_chance = face_chance
        self._action_chance = action_chance
        self._exclamation_chance = exclamation_chance
        self._nsfw_actions = nsfw_actions

    def _uwuify_words(self, _msg):
        # split the message into words
        words = _msg.split(" ")

        # iterate over each individual word
        # sure you could regex the entire thing, but then you lose
        # the ability to ignore certain cases, like pings and urls
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue

            # skip URIs and URNs
            if re.search(
                URI_REGEX,
                word,
            ):
                continue

            # skip pings
            if word[0] == "@" or word[0] == "#" or word[0] == ":" or word[0] == "<":
                continue

            # for each pattern in the array
            for pattern, substitution in self._uwu_patterns:
                # attempt to use the pattern on the word
                word = re.sub(pattern, substitution, word)

            # add the modified word to the original words array
            words[idx] = word

        # return the joined string
        return " ".join(words)

    def _uwuify_spaces(self, _msg):
        # split the message into words
        words = _msg.split(" ")

        # iterate over each individual word
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue

            # skip URIs and URNs
            if re.search(
                URI_REGEX,
                word,
            ):
                continue

            # S-s-s-skip nyon wettews, to avoid ( ᵘ ꒳ ᵘ ✼) s-s-s-stuttews like: /-/-///
            # This checks if the chaw is a wettew
            if not unicodedata.category(word[0]).lower().startswith("l"):
                continue

            stutter = ""

            if random.random() <= self._stutter_chance:
                # Adds a l- from 1 up to 3 times
                stutter += "".join([f"{word[0]}-" for _ in range(random.randint(1, 3))])

            # Then we join e.g. e-e-e + e + rest_of_the_word
            _word = stutter + word[0] + word[1:]

            # if we are to add a face, do it
            if random.random() <= self._face_chance:
                _word = (_word or word) + " " + random.choice(self.__faces)

            # if we are to add an action, do it
            if random.random() <= self._action_chance:
                _word = (
                    (_word or word)
                    + " "
                    + random.choice(
                        self.__actions
                        if not self._nsfw_actions
                        else self.__actions + self.__nsfw_actions
                    )
                )

            # replace the word in the array with the modified if it exists, if not add the original word back
            words[idx] = _word or word

        return " ".join(words)

    def _uwuify_exclamations(self, _msg):
        # split the message into words
        words = _msg.split(" ")

        # iterate over each individual word
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue

            # skip if an exclamation is not present or the random number is greater than the chance
            if (
                not re.search(r"[?!]+$", word)
            ) or random.random() > self._exclamation_chance:
                continue

            # strip the exclamation from the word, add new exclamations and return it to the words array
            word = re.sub(
                r"([?!]+)$",
                lambda mtch: random.choice(
                    self.__exclamations["?" if "?" in mtch[1] else "!"]
                ),
                word,
            )
            words[idx] = word

        # return the joined string
        return " ".join(words)

    def uwuify(self, msg):
        msg = self._uwuify_words(msg)
        msg = self._uwuify_spaces(msg)
        msg = self._uwuify_exclamations(msg)

        return msg
