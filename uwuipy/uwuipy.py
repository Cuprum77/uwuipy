import re
import random
from typing import Union
import unicodedata


class uwuipy:
    __uwu_pattern = [
        (r"[rl]", "w"),
        (r"[RL]", "W"),
        (r"n([aeiou])", r"ny\g<1>"),
        (r"N([aeiou])", r"Ny\g<1>"),
        (r"N([AEIOU])", r"NY\g<1>"),
        (r"ove", "uv"),
        (r"pog", "poggies"),
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
        "***smirks smuggly***",
        "***breaks into your house and aliases neofetch to rm -rf --no-preserve-root /***",
    ]

    # Because I got annoyed at them not being toggleable.
    __nsfw_actions = [
        "***twerks***",  # arguably nsfw
        "***sees bulge***",
        "***notices buldge***",
        "***starts twerking***",  # also arguable.
        "***unzips your pants***",
        "***pounces on your buldge***",
    ]

    __exclamations = [
        "!?",
        "?!!",
        "?!?1",
        "!!11",
        "!!1!",
        "?!?!",
    ]

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
    ):
        # input protection to make sure the user stays within allowed parameters
        if not 0.0 <= stutter_chance <= 1.0:
            raise ValueError(
                "Invalid input value for stutterChance, supported range is 0-1.0"
            )
        if not 0.0 <= face_chance <= 1.0:
            raise ValueError(
                "Invalid input value for faceChance, supported range is 0-1.0"
            )
        if not 0.0 <= action_chance <= 1.0:
            raise ValueError(
                "Invalid input value for actionChance, supported range is 0-1.0"
            )
        if not 0.0 <= exclamation_chance <= 1.0:
            raise ValueError(
                "Invalid input value for exclamationChance, supported range is 0-1.0"
            )

        random.seed(seed)
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
            # skip URLs
            if re.search(r"((http:|https:)//[^ \<]*[^ \<\.])", word):
                continue
            # skip pings
            if word[0] == "@" or word[0] == "#" or word[0] == ":" or word[0] == "<":
                continue
            # for each pattern in the array
            for pattern, substitution in self.__uwu_pattern:
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
            word = re.sub(r"[?!]+$", "", word) + random.choice(self.__exclamations)
            words[idx] = word

        # return the joined string
        return " ".join(words)

    def uwuify(self, msg):
        msg = self._uwuify_words(msg)
        msg = self._uwuify_spaces(msg)
        msg = self._uwuify_exclamations(msg)

        return msg
