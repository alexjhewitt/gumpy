"""
Gumpy is a Python library that provides a set 
of utilities for building command-line interfaces.
"""

import subprocess

def choose(prompt: str = None, options: list = None, limit: int = 1) -> list:
    """Choose an option from a list of choices.

    Args:
        question (str): The question to ask the user (optional).
        options (list): A list of choices to present to the user.
        limit (int, optional): How many choices can be selected. Defaults to 1.

    Returns:
        list: A list of the user's choices.
    """
    command = f"gum choose --limit={limit} " + " ".join(options)
    if prompt : print(prompt)
    result = subprocess.run(command.split(" "), stdout=subprocess.PIPE, text=True, check=True)
    if result.returncode != 0:
        print(result.stderr)

def confirm():
    raise NotImplementedError("This function is not implemented yet")

def file():
    raise NotImplementedError("This function is not implemented yet")

def format():
    raise NotImplementedError("This function is not implemented yet")

def input():
    raise NotImplementedError("This function is not implemented yet")

def join():
    raise NotImplementedError("This function is not implemented yet")

def pager():
    raise NotImplementedError("This function is not implemented yet")

def spin():
    raise NotImplementedError("This function is not implemented yet")

def style():
    raise NotImplementedError("This function is not implemented yet")

def table():
    raise NotImplementedError("This function is not implemented yet")

def write():
    raise NotImplementedError("This function is not implemented yet")

def log():
    raise NotImplementedError("This function is not implemented yet")



