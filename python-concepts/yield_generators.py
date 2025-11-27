"""
Example to demonstrate how yield keyword and generator type function works

A yield function pauses the function after preprocessing and does not execute until it is called again.
It holds the current value of the function while it is being executed.

When the yield is defined, value is returned back to the caller as a "Generator" iterator.
Calling the function again continues the function execution from its current point. A benefit of using yield is that it
does not add up any memory while doing the pause/blocking call.

A practical use of yield can be in CSV file processing where a preprocessing is done, returned to parent function to
further process the same line. Once current line processing is complete, another function can invoke the generator
iterator to make the function read the next line for processing.
"""
from typing import Generator


def generate_odd_nums(limit: int) -> Generator[int, None, None]:
    i = 1
    while i < limit:
        print(f"Value of I is {i}")
        yield i
        print(f"After yielding {i}")
        i += 2
        print(f"After incrementing: {i}")


if __name__ == '__main__':
    generator = generate_odd_nums(10)
    print(generator, type(generator))  # first iteration, prints start of sequence
    while True:
        try:
            print("Back to function, executing generator again")
            print(next(generator))
        except StopIteration:
            print(f"Generator stopped due to stop condition")
            break
