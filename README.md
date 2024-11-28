# learn-python repository

## Udemy - Automate with Python

* Python refresher course <br/>
* Projects and code : <br/>
  Refer repository directory: [udemy-automate-with-python](udemy-automate-with-python/README.md)

## Python basics

**Reading book - Python crash course 3rd edition by Eric Mathes**

### Start a python virtualenv

```commandline
python3 -m venv venv
source venv/bin/activate
```

**See - [string_basics.py](python-crash-course-3rd-ed/string_basics.py)**

* 101 - Install, Know how to print, compile and run python programs
* Write comments - `#`
* String key concepts:
    * `f"` to format strings shell style - `f"{first_name} {last_name}`
    * String case conversions - `title()`, `upper()`, `lower()`
    * newlines and tabs - `\n` and `\t`
    * stripping whitespace - `lstrip()`, `rstrip()`, `strip()`
    * prefix methods - `removePrefix()`, `removeSuffix()`

Skipping practice for number basics -

- REPL shell - `+`, `-`
- Using underscores in numbers to make it more readable

**See [list_basics.py](python-crash-course-3rd-ed/list_basics.py)**

* List basics - add elements, find elements, remove elements
* Sorting a list - `sort()`, `sorted()`, `reverse()`, `sort(reverse=True)`
* List Comprehension
* List slicing
* List copying

Recollection questions-

- What is the difference between `sort()` and `sorted()`?
- What is the difference between `reverse()`, and `sort(reverse=True)`?
- How to retrieve last element from a list?
- How to slice a list?
- What is the index inclusion/exclusion in a range(0, 10) ?
- What is the index inclusion/exclusion in a slice[0:10] ?

**See [loop_basics.py](python-crash-course-3rd-ed/loop_basics.py)**

* Simple for loop
* Numerical loops with range
* Iterating a sliced list
* loops with list comprehension

**See [tuples_basics.py](python-crash-course-3rd-ed/tuples_basics.py)**

* A tuple is an "unmodifiable" or "immutable" list
* List -> Tuple, Tuple -> List
* Slicing a tuple
* iterating a tuple

**See [conditional_basics.py](python-crash-course-3rd-ed/conditionals_basics.py)**

* learn `if-else-elif` pattern
* learn usage of `in` and `not in` pattern
* iterating through list using conditionals along the way

**See [dictionary_basics.py](python-crash-course-3rd-ed/dictionary_basics.py)**

* Using dictionaries
* Iterating dictionaries
* Accessing nested dictionaries