# uwuipy
An advacned uwuifier for python.
## Install
To install just use PyPI `pip install uwuipy`
## Usage
Basic usage for uwuifying user input.
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

the seed sets the rng seed for the random events, and the values for the paramers (range is between 0 and 1.0) controll the probablity of them occuring.
```python
from uwuipy import uwuipy

uwu = uwuipy(None, 0.3, 0.3, 0.3, 1)
print(uwu.uwuify(input()))
```
you can use an integer seed (for example the timestamp when a messag was posted to give it a unique uwuify)
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

Licenced under [MIT](./LICENSE)
