from __future__ import annotations

import re
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union

import unicodedata


URI_REGEX = r"(?:[a-zA-Z]+:)+/*(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

SPECIAL_TOKEN_REGEX = re.compile(
    r"(@everyone|@here)|"          # global mentions
    r"(<a?:[a-zA-Z0-9_]+:\d+>)|"   # real Discord emoji <a:name:id>
    r"(:[a-zA-Z0-9_]+:)|"          # potential plain emoji :name:
    r"(<[@#!][^>]+>)|"             # mentions/channels/roles <@123>, <#123>
    + URI_REGEX                    # URLs
)

SPACE_TOKENIZER = re.compile(r"(\s+)")

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

    def _uwuify_words(self, _msg, skip_urls=True):
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
            if skip_urls and re.search(
                URI_REGEX,
                word,
            ):
                continue

            # use the uwuify_segmented method instead for better handling of special tokens
            # skip pings
            # if word[0] == "@" or word[0] == "#" or word[0] == ":" or word[0] == "<":
            #     continue

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
    
    def uwuify_segmented(
        self,
        msg: str,
        verify_urls: bool = False,
        verify_men_chan_role: bool = True,
        verify_emojis: bool = True,
    ) -> list[tuple[str | None, str | None, bool]]:
        """
        Uwuifies a message while preserving or marking special tokens such as URLs,
        mentions, channels, roles, and emojis.

        This method scans the input string, identifies special Discord-style tokens
        (for example ``https://...``, ``<@123>``, or ``:emoji_name:``), and returns
        each text segment alongside its uwuified version. The caller can then decide,
        based on the boolean flags, whether to keep the original segment (for real
        mentions or emojis) or use the uwuified one.

        :param msg:  
            The message text to uwuify.

        :param verify_urls:  
            If ``True``, URL-like tokens are marked as special and require caller
            verification. If ``False``, URLs are left untouched and not marked as
            special. Defaults to ``False``.

        :param verify_men_chan_role:  
            If ``True``, Discord mentions (``<@123>``), channels (``<#123>``),
            and roles (``<@&123>``) are marked as special tokens.
            If ``False``, they are preserved automatically. Defaults to ``True``.

        :param verify_emojis:  
            If ``True``, both custom Discord emojis (``<:name:id>``, ``<a:name:id>``)
            and plain-text emoji syntax (``:name:``) are marked as special tokens.
            If ``False``, they are left untouched and not marked as special.
            Defaults to ``True``.

        :returns:  
            A list of tuples in the format ``(original_segment, uwuified_segment, is_special_token)``

            * **original_segment** – The exact text from the input, or ``None`` if the uwuified
              output inserted new content (e.g., actions or faces).
            * **uwuified_segment** – The uwuified version of that text.
            * **is_special_token** – ``True`` if this segment might represent a URL,
              emoji, mention, etc. The caller can verify and choose which version to use.
        """
        SPACE_TOKENIZER = re.compile(r"(\s+)")  # capture and preserve spaces
        result = []
        last_end = 0

        for match in SPECIAL_TOKEN_REGEX.finditer(msg):
            start, end = match.span()
            token = msg[start:end]

            # Handle preceding normal text
            if start > last_end:
                chunk = msg[last_end:start]

                # Fully uwuify before tokenizing spaces
                uwuified_chunk = self._uwuify_exclamations(
                    self._uwuify_spaces(self._uwuify_words(chunk))
                )

                # Split both into atomic tokens (spaces + words)
                orig_parts = SPACE_TOKENIZER.split(chunk)
                uwu_parts = SPACE_TOKENIZER.split(uwuified_chunk)

                # Merge keeping inserts from uwuified version
                max_len = max(len(orig_parts), len(uwu_parts))
                for i in range(max_len):
                    o = orig_parts[i] if i < len(orig_parts) else None
                    u = uwu_parts[i] if i < len(uwu_parts) else None
                    if not o and not u:
                        continue
                    result.append((o, u, False))

            # Identify token type
            is_url = bool(re.match(URI_REGEX, token))
            is_men_chan_role = (
                bool(re.match(r"^<[@#!][^>]+>$", token))
                or token in {"@everyone", "@here"}
            )
            is_emoji = bool(re.match(r"^<a?:[a-zA-Z0-9_]+:\d+>$", token)) or bool(
                re.match(r"^:[a-zA-Z0-9_]+:$", token)
            )

            # Decide how to handle based on flags
            if (is_url and not verify_urls) or \
               (is_men_chan_role and not verify_men_chan_role) or \
               (is_emoji and not verify_emojis):
                # Automatically handled — no verification needed
                result.append((token, token, False))
            else:
                # Needs verification — uwuify for comparison
                uwu_token = self._uwuify_exclamations(
                    self._uwuify_spaces(self._uwuify_words(token))
                )
                result.append((token, uwu_token, True))

            last_end = end

        # Handle trailing text
        if last_end < len(msg):
            chunk = msg[last_end:]
            uwuified_chunk = self._uwuify_exclamations(
                self._uwuify_spaces(self._uwuify_words(chunk))
            )

            orig_parts = SPACE_TOKENIZER.split(chunk)
            uwu_parts = SPACE_TOKENIZER.split(uwuified_chunk)

            max_len = max(len(orig_parts), len(uwu_parts))
            for i in range(max_len):
                o = orig_parts[i] if i < len(orig_parts) else None
                u = uwu_parts[i] if i < len(uwu_parts) else None
                if not o and not u:
                    continue
                result.append((o, u, False))

        return result

    def uwuify(self, msg, skip_urls=True) -> str:
        msg = self._uwuify_words(msg, skip_urls=skip_urls)
        msg = self._uwuify_spaces(msg)
        msg = self._uwuify_exclamations(msg)

        return msg
