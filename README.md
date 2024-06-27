# uwuipy
`uwuipy` is an advanced uwuifier for Python, designed to transform regular text into a playful and expressive "uwu" style. This whimsical modification of text is often used in online communities for humorous or emotive communication.

Whether you're looking to add a fun twist to a chat application or simply want to explore text manipulation in a lighthearted manner, `uwuipy` offers an easy-to-use interface with customizable options to create unique text transformations.

The library provides control over various aspects of the uwuification process, including stuttering, facial expressions, actions, and exclamations. Whether you want subtle changes or dramatic transformations, `uwuipy` allows you to find the perfect balance through adjustable parameters.

## Key Features:
- Ease of Use: Quickly integrate `uwuipy` into your projects with a simple API.
- Customizable: Tailor the uwuification process to your needs with adjustable parameters.
- CLI Support: Use the tool directly from the command line or integrate it into Python applications.
- Entertainment: A unique way to engage users with lively and animated text transformations.

## Requirements
* Python 3.10 or higher

## Install
To install just use PyPI `pip install uwuipy`

## Usage
### As a library
Integrate `uwuipy` into your Python application to transform ordinary text into playful uwu-styled expressions. Here's a basic example of how to use it:
```python
from uwuipy import Uwuipy

uwu = Uwuipy()
print(uwu.uwuify(input()))
```

#### Constructor parameters
The `Uwuipy` constructor allows fine-tuning of the uwuification process through the following parameters:

- `seed`: An integer seed for the random number generator. Defaults to current time if - not provided.
- `stutterchance`: Probability of stuttering a word (0 to 1.0), default 0.1.
- `facechance`: Probability of adding a face (0 to 1.0), default 0.05.
- `actionchance`: Probability of adding an action (0 to 1.0), default 0.075.
- `exclamationchance`: Probability of adding exclamations (0 to 1.0), default 1.
- `nsfw_actions`: Enables more "explicit" actions if set to true; default is false.
- `power`: The uwuification "level" — higher levels lead to more text transformations being done (1 is core uwu, 2 is nyaification, 3 and 4 are just extra). Using a higher level includes the lower levels.

#### Customized Example:
Adjust the parameters to create a customized uwuification process:
```python
from uwuipy import Uwuipy

uwu = Uwuipy(None, 0.3, 0.3, 0.3, 1, False, 4)
print(uwu.uwuify(input()))
```

This can produce output like:
```
The quick bwown (ᵘʷᵘ) ***glomps*** f-f-fox jyumps uvw the ***screeches*** w-w-w-wazy ***blushes*** dog
The (ᵘﻌᵘ) quick bwown ***smirks smugly*** fox \>w\< ***screeches*** jyumps uvw t-t-t-the (uwu) wazy owo dog ~(˘▾˘~)
The q-q-q-quick ***nuzzles your necky wecky*** b-b-bwown f-f-fox ( ᵘ ꒳ ᵘ ✼) j-j-jyumps (U ﹏ U) u-uvw ***whispers to self*** the owo w-w-w-wazy Uwu d-d-d-dog ***huggles tightly***
```

#### Time-Based Seeding:
Utilize time-based seeding for unique transformations:
```python
from datetime import datetime
from uwuipy import Uwuipy

message = "Hello this is a message posted in 2017."
seed = datetime(2017, 11, 28, 23, 55, 59, 342380).timestamp()
uwu = Uwuipy(seed)
print(uwu.uwuify(message))  # Hewwo ***blushes*** t-t-t-this is a ***cries*** message posted ***screeches*** in 2017.
```
This method only uses the `uwuify()` function, accepting a string and returning an uwuified string based on the constructor parameters.

### Directly in the terminal
#### CLI
Use `uwuipy` directly from the command line for quick uwuification:
```bash
python3 -m uwuipy The quick brown fox jumps over the lazy dog
```
Output:
```bash
The q-q-quick bwown fox jyumps uvw the wazy dog
```

#### REPL
REPL Mode:
```bash
python3 -m uwuipy 
>>> The quick brown fox jumps over the lazy dog
The quick bwown fox jyumps uvw the wazy dog
```

#### Help
Command Line Help:
```bash
python3 -m uwuipy --help
```

## Contributing and Licence
Feel free contribute to the [GitHub repo](https://github.com/Cuprum77/uwuipy) of the project.

Licenced under [MIT](https://github.com/Cuprum77/uwuipy/blob/main/LICENSE)
