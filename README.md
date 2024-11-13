# gumpy
gumpy is a Python implementation of charm.sh's CLI tool called [gum](https://github.com/charmbracelet/gum). Gum is used to create aesthetically pleasing shell scripts. 

# Installation
Install gum for your environment using the [instructions](https://github.com/charmbracelet/gum).
Then install my python package like so:
```sh
$ git clone https://github.com/alexjhewitt/gumpy.git
$ cd gumpy
$ python3 setup.py install
```

# Usage
```python
import gumpy


```

# Note
Not all command flag options in the gum library are given for each command. 
E.g. `gum choose` for example allows for a limit which I have included functionality for, but there are other [options](https://github.com/charmbracelet/gum/blob/main/choose/options.go) such as `CursorPrefix` that are not included for simplicity's sake. 