import functools
import random


# Exercise 3.1


def inspect(*args, **kwargs):
    print(f"args type: {type(args)}") # always tuple
    print(f"kwargs type: {type(kwargs)}") # always dict
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

inspect(1, 2, 3) # args: (1, 2, 3) kwargs: {}
inspect(a=1, b=2) # args: () kwargs {"a": 1, "b": 2}
inspect(1, 2, x=3, y=4) # args: (1, 2) kwargs: {"x": 3, "y": 4}
inspect() # args: () kwargs {}

def mean(*numbers: float) -> float:
    """Return the mean of any number of floats"""

    return sum(numbers) / len(numbers)

def create_model_config(model_type: str, **hyperparams) -> dict:
    """
    Return a config dict with model_type and all hyperparams.
    Example: create_model_config("mlp", lr=0.001, hidden=128)
    -> {"model_type": "mlp", "lr": 0.001, "hidden": 128}
    """
    model_config = {
        "model_type": model_type
    }

    model_config.update(hyperparams)

    return model_config

def run_experiment(dataset: str, *metrics: str, verbose: bool = False, **model_kwargs):
    """
    Mixed signature: positional *args, keywords-only, **kwargs
    Print a summary of the experiment configuration
    """

    print(f"Dataset: {dataset}")
    print("Metrics:")
    for metric in metrics:
        print(f"- {metric}")
    print(f"Verbose: {verbose}")
    for key, value in model_kwargs.items():
        print(f"{key}: {value}")


print(mean(1, 2, 3, 4, 5)) # 3.0
print(mean(10.0, 20.0)) # 15.0
cfg = create_model_config("transformer", layers=6, heards=8, lr=0.0001)
assert cfg["model_type"] == "transformer"
assert cfg["layers"] == 6
run_experiment("Skibidi3", "good", "eye", "turbo", lr=0.001, epochs=8, batch_size=32)



# Exercise 3.2


def merge_configs(*dicts: dict) -> dict:
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged

assert merge_configs({"a": 1}, {"b": 2}, {"a": 3}) == {"a": 3, "b": 2}

def train(model, optimizer, loss_fn, *, epochs=10, device="cpu"):
    pass

base = {"epochs": 5, "device": "cuda"}

train(None, None, None, **base)
train(None, None, None, epochs=8)
# train(None, None, None, 10, "cuda") Doesn't work because of * in parameters. * forces parameters after
# it to take only keyword arguments. So we are passing 5 positional arguments which is too much (need 3)


# Exercise 3.3


def outer(x):
    def inner(y):
        return x + y
    return inner

add_10 = outer(10)
add_20 = outer(20)

print(add_10(5)) # 15
print(add_20(5)) # 25
print(add_10(add_20(0))) # 30

functions = []
for i in range(5):
    functions.append(lambda: i)

print([f() for f in functions]) # [4, 4, 4, 4, 4]

functions_fixed = []
for i in range(5):
    functions_fixed.append(lambda i=i: i)

print([f() for f in functions_fixed])

def make_multiplier(factor: float):
    """Return a function that multiplies its input by factor"""
    def inner(x):
        return factor * x
    return inner

def make_counter(start: int = 0, step: int = 1):
    """
    Return a counter function. Each call return the next value.
    Use nonlocal to mutate the captured variable.
    """
    count = start
    def counter():
        nonlocal count
        count_before_step = count
        count += step
        return count_before_step
    return counter

def make_running_average():
    """
    Return a function that accepts one number at a time
    and returns the running average of all numbers seen so far.
    """

    numbers = []
    def inner(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)

    return inner

triple = make_multiplier(3)
assert triple(5) == 15
assert triple(10) == 30

c = make_counter(start=0, step=2)
assert c() == 0
assert c() == 2
assert c() == 4

avg = make_running_average()
assert avg(10) == 10.0
assert avg(20) == 15.0
assert avg(30) == 20.0


# Exercise 3.4


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print("done")
        return result
    return wrapper

@trace
def add(a, b):
    return a + b

assert add(3, 4) == 7

def repeat(n: int):
    """Calls the decorated function n times, return nthe last result."""
    
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("hello")

say_hello()

def memoize(func):
    """Cache results. Same arguments -> return cached result."""

    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))

def typecheck(func):
    """
    Verify that all arguments match the function's type hints at call time.
    Raise TypeError with a clear message if they don't.
    Use func.__annotations__ to get hints.
    """

    import inspect

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound = inspect.signature(func).bind(*args, **kwargs)
        bound.apply_defaults()
        for key, value in bound.arguments.items():
            if not isinstance(value, func.__annotations__[key]):
                raise TypeError("Value doesn't match its annotated type")
        result = func(*args, **kwargs)
        return result

    return wrapper

@typecheck
def power(base: float, exponent: int) -> float:
    return base ** exponent

print(power(2.0, 3))
# print(power(2.0, 3.5)) # TypeError
# print(power("two", 3)) # TypeError



# Exercise 3.5


def countdown(n: int):
    """Yield n, n-1, n-2, ..., 1, 0"""
    for i in range(n + 1):
        yield n - i


gen = countdown(6)
for i in gen:
    print(i)


def fibonacci_gen():
    """Infinite generator of Fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
first_10 = list(islice(fibonacci_gen(), 10))
print(first_10)

def read_numbers(path: str):
    """Yield one integrer per line from a file, skipping blank lines"""
    with open(path) as f:
        for line in f:
            stripped = line.strip()
            if stripped != "":
                yield int(stripped)

def filter_even(numbers):
    """Yield only even numbers from an iterable"""
    for number in numbers:
        if number % 2 == 0:
            yield number 

gen = filter_even([1,2,3,4,5,6,7,8,9])
for i in gen:
    print(i)

def square_each(numbers):
    """Yield x**2 for each x in numbers"""
    for x in numbers:
        yield x ** 2

gen = square_each([1,2,3,4,5])
for i in gen:
    print(i)

# pipeline = square_each(filter_even(read_numbers("data.txt")))
chain = list(square_each(filter_even(range(20))))
print(chain)

def batch_generator(data: list, batch_size: int, shuffle: bool = False, seed: int = 42):
    """
    Yield batches of data.
    If shuffle=True, shuffle the data before batching.
    The last batch may be smaller than batch_size.
    """
    random.seed(seed)

    data_copy = data.copy()
    if shuffle:
        random.shuffle(data_copy)

    for start in range(0, len(data), batch_size):
        yield data_copy[start : start + batch_size]

data = list(range(10))
batches = list(batch_generator(data, batch_size=3))
print(batches)

assert len(batches[-1]) == 1

batches_shuffled = list(batch_generator(data, batch_size=3, shuffle=True))
flat = [x for batch in batches_shuffled for x in batch]
assert sorted(flat) == data