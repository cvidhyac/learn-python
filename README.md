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
* Find Size of a list or tuple
* How to check if list is empty?
* How to check if list is not empty?
* Remove duplicates from a list

Recollection questions-

- What is the difference between `sort()` and `sorted()`?
- What is the difference between `reverse()`, and `sort(reverse=True)`?
- How to retrieve last element from a list?
- How to slice a list?
- What is the index inclusion/exclusion in a range(0, 10) ?
- What is the index inclusion/exclusion in a slice[0:10] ?

**See [loop_basics.py](python-crash-course-3rd-ed/loop_basics.py)**

* Simple for loop
* How to exit a for loop if something is found?
* Numerical loops with range
* Iterating a sliced list
* loops with list comprehension

**See [tuples_basics.py](python-crash-course-3rd-ed/tuples_basics.py)**

* A tuple is an "unmodifiable" or "immutable" list
* List -> Tuple, Tuple -> List
* Slicing a tuple
* iterating a tuple
* Merge two lists - 2 techniques - using `+`, using extend() - recollect what is the difference in these two techniques

**See [conditional_basics.py](python-crash-course-3rd-ed/conditionals_basics.py)**

* learn `if-else-elif` pattern
* learn usage of `in` and `not in` pattern
* iterating through list using conditionals along the way

**See [dictionary_basics.py](python-crash-course-3rd-ed/dictionary_basics.py)**

* Using dictionaries
* Modifying value in a dictionary for one of the keys
* Deleting a key from a dictionary
* What is the difference between using square brackets to retrieve a value from a dictionary vs using `get()`
* Iterating dictionaries using `items()`, `keys()`, `values()`
* What is the default behaviour neither of the 3 options above for items, keys values are not specified in
  looping condition?
* Accessing elements from dictionaries
* How to convert a dictionary to kwargs?
* Printing kwargs, accessing individual elements in kwargs

**See [user_inputs.py](python-crash-course-3rd-ed/user_inputs.py)**

* User inputs
* `while` loop - repeating user input until condition is not satisfied
* How to exit a `while` loop?
* Can you think of a way to populate a dictionary using user inputs?

**Function basics See - [functions_basics.py](python-crash-course-3rd-ed/functions_basics.py)**

* What are the 2 ways of passing arguments to functions? What is the default?
* How to pass keyword arguments to pass values to functions?
* Pitfalls of positional arguments?
* How to make a specific argument passed to a method as optional? 
  - for e.g., - among first_name, middle_name, last_name how to make middle_name optional
* How to prevent a function from modifying an original copy of a `list` data structure?
* How to pass arbitrary number of arguments(varargs) in a python function (eg. a list of 3 toppings or 5)?
* What is used to collect non-specific function arguments in a python function?

* Are there any restrictions in where the positional arguments or kwargs can be located in a function declaration?
  (hint: yes, at the end)
* How to import all the functions in a module?
* How does relative import work in python - how to import projects/restaurants/restaurant.py in projects/tryit/ex1.py
* What is the IDE setting if imports doesnt resolve (hint: Mark as sources root)

**Working with Classes, see - [Classes exercises](python-crash-course-3rd-ed/tryit)**

* [Example with class instantiation and relative imports](python-crash-course-3rd-ed/relative_imports.py)
* How does inheritance work in python?
* How to access variables in parent class in child class?
* How to import multiple classes from a module?
* How to import entire module?
* How does alias help in imports?

**Python Standard library**
* Example for `random` and using `randInt`, see [Random Dice](python-crash-course-3rd-ed/random_dice.py)
* Example for `random.sample`, see [Lottery analysis](python-crash-course-3rd-ed/lottery_analysis.py)
* Class naming conventions (hint: )

## Extra exercises

* Finding ordinal number prefixes for given number range