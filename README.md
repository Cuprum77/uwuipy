
# uwuipy
An advanced uwuifier for python.
## Install
To install just use PyPI `pip install uwuipy`
## Usage
Usage from CLI:
```bash
python3 -m uwuipy The quick brown fox jumps over the lazy dog
The quick b-b-b-bwown (・\`ω\´・) ***screeches*** fox jumps uvw t-t-t-the OwO wazy dog
```

It can also be used as a REPL:
```bash
python3 -m uwuipy 
>>> The quick brown fox jumps over the lazy dog
The quick b-b-b-bwown (・\`ω\´・) ***screeches*** fox jumps uvw t-t-t-the OwO wazy dog
>>> ^D
```

For explanations of the CLI flags please run
```bash
python3 -m uwuipy --help
```

Basic usage as a library for uwuifying user input:
```python
from uwuipy import uwuipy

uwu = uwuipy()
print(uwu.uwuify(input()))
```
The constructor accepts several optional parameters:
* seed
* stutterchance
* facechance
* actionchance
* exclamationchance

the seed sets the rng seed for the random events, and the values for the parameters (range is between 0 and 1.0) control the probability of them occuring.
```python
from uwuipy import uwuipy

uwu = uwuipy(None, 0.3, 0.3, 0.3, 1)
print(uwu.uwuify(input()))
```
Usage of the above example:
```
The quick brown fox jumps over the lazy dog
The quick b-b-b-bwown (・\`ω\´・) ***screeches*** fox jumps uvw t-t-t-the OwO wazy dog
```
You can use an integer seed (for example the timestamp when a message was posted to give it a unique uwuify)
```python
from datetime import datetime
from uwuipy import uwuipy

message = "Hello this is a message posted in 2017."
seed = datetime(2017, 11, 28, 23, 55, 59, 342380).timestamp()
uwu = uwuipy(seed)
print(uwu.uwuify(message))
```
as you can see we only use one method `uwuify()` it accepts a string and returns an uwuified string as per the values set in the contructor.
## Contributing and Licence
Feel free contribute to the [github repo](https://github.com/Cuprum77/uwuipy) of the project.

Licenced under [MIT](https://github.com/Cuprum77/uwuipy/blob/main/LICENSE)
