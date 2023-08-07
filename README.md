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
from uwuipy import uwuipy

uwu = uwuipy()
print(uwu.uwuify(input()))
```

#### Constructor parameters
The `uwuipy` constructor allows fine-tuning of the uwuification process through the following parameters:

- `seed`: An integer seed for the random number generator. Defaults to current time if - not provided.
- `stutterchance`: Probability of stuttering a word (0 to 1.0), default 0.1.
- `facechance`: Probability of adding a face (0 to 1.0), default 0.05.
- `actionchance`: Probability of adding an action (0 to 1.0), default 0.075.
- `exclamationchance`: Probability of adding exclamations (0 to 1.0), default 1.
- `nsfw_actions`: Enables more explicit actions if set to true; default is false.

#### Customized Example:
Adjust the parameters to create a customized uwuification process:
```python
from uwuipy import uwuipy

uwu = uwuipy(None, 0.3, 0.3, 0.3, 1, False)
print(uwu.uwuify(input()))
```

This can produce output like:
```
The quick brown fox jumps over the lazy dog
The quick b-b-b-bwown (・\`ω\´・) ***screeches*** fox jumps uvw t-t-t-the OwO wazy dog
```

#### Time-Based Seeding:
Utilize time-based seeding for unique transformations:
```python
from datetime import datetime
from uwuipy import uwuipy

message = "Hello this is a message posted in 2017."
seed = datetime(2017, 11, 28, 23, 55, 59, 342380).timestamp()
uwu = uwuipy(seed)
print(uwu.uwuify(message))
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
The quick b-b-b-bwown (・\`ω\´・) ***screeches*** fox jumps uvw t-t-t-the OwO wazy dog
```

#### REPL
REPL Mode:
```bash
python3 -m uwuipy 
>>> The quick brown fox jumps over the lazy dog
The quick b-b-b-bwown (・\`ω\´・) ***screeches*** fox jumps uvw t-t-t-the OwO wazy dog
```

#### Help
Command Line Help:
```bash
python3 -m uwuipy --help
```

## Contributing and Licence
Feel free contribute to the [GitHub repo](https://github.com/Cuprum77/uwuipy) of the project.

Licenced under [MIT](https://github.com/Cuprum77/uwuipy/blob/main/LICENSE)
