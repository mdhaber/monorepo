# bad_typing.py

# Function without type annotations (this will trigger an error with strict=True)
def add(a, b):
    return a + b


# Function with missing type annotations (strict=True will flag this)
def greet(name):
    return "Hello " + name


# Function with type annotations (this will pass in both strict and non-strict modes)
def multiply(a: int, b: int) -> int:
    return a * b


# Function with implicit return type (only strict=True will flag this)
def get_value():
    return 42


# Function with an untyped call (only strict=True will flag this)
def call_add():
    return add(5, 10)  # `add` is untyped, so it will be flagged in strict mode
