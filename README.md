# learn-python repository

## Learning resources

I used the following learning resources to document my learning journey and for keeping
track of how well I can recollect the concepts after taking a break.

### Udemy - Automate with Python

* Python refresher course (I don't recollect which one i used) <br/>
* Projects and code : <br/>
  Refer repository directory: [udemy-automate-with-python](udemy-automate-with-python/README.md)

From my personal experience taking this route, I learned that while online courses are good for basics,
they are unable to cover the depth you could gain by reading ONE book.

### Python Books

These are the books that i have used for my personal learning journey and for practice.

- [Automate Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python crash course 3rd edition by Eric Mathes](https://ehmatthes.github.io/pcc_3e/)
- [Learning Python, sixth edition](https://learning-python.com/about-lp6e.html)

## Refresher Notes

### Start a python virtualenv

```commandline
python3 -m venv venv
source venv/bin/activate
```

**See - [string_basics.py](python-concepts/string_basics.py)**

* 101 - Install, Know how to print, compile and run python programs
* Write comments - `#`
* String key concepts:
    * `f"` to format strings shell style - `f"{first_name} {last_name}`
    * String case conversions - `title()`, `upper()`, `lower()`
    * newlines and tabs - `\n` and `\t`
    * stripping whitespace - `lstrip()`, `rstrip()`, `strip()`
    * prefix methods - `removePrefix()`, `removeSuffix()`
* Can you slice a string? What is the rule to remember when slicing?
* How to reverse a string
* How to find a substring within a given string
* What is the difference between `find` and `index` methods in string?

**See - [operators_basics.py](python-concepts/operators_basics.py)**
* What are the membership check operators in python?
* What are the common operators in python?
* What is the difference between `//` and `/` division operator in python? (Hint: Integer division vs floating point)
* What are the membership operators in python?
* What are the identity operators in python?
* Explain Operator Precedence (hint: P E D M A S rule)

**See [Shallow vs deep copy](python-concepts/shallow-deep-copy.py)
* What is the difference between shallow and deep copy?
* What are the immutable data types in python, which are mutable?
* Explain Python pass-by-object-reference concept, how to make data immutable, what are the equivalent immutable types
of mutable types?

Skipping practice for number basics -

- REPL shell - `+`, `-`
- Using underscores in numbers to make it more readable

**See [list_basics.py](python-concepts/list_basics.py)**

* List basics - add elements, find elements, remove elements
* Sorting a list - `sort()`, `sorted()`, `reverse()`, `sort(reverse=True)`
* List Comprehension
* List slicing
* List copying
* Find Size of a list or tuple
* How to check if list is empty?
* How to check if list is not empty? (Hint: Implicit boolean, pythonic)
* Remove duplicates from a list
* How to skip count in a list?
* What is the difference between sequence-controlled iteration and sentinel controlled iteration?
* Explain how tuple unpacking works? when is it useful? (hint: see [gcd-with-tuple-unpacking](practice/greatest-common-divisor.py))

Recollection questions-

- What is the difference between `sort()` and `sorted()`?
- What is the difference between `reverse()`, and `sort(reverse=True)`?
- How to retrieve last element from a list?
- How to slice a list?
- What is the index inclusion/exclusion in a range(0, 10) ?
- What is the index inclusion/exclusion in a slice[0:10] ?
- How to replace a slice of a list with another list? see - [slicing_tricks](python-concepts/list_basics.py)

**See [loop_basics.py](python-concepts/loop_basics.py)**

* Simple for loop
* How to exit a for loop if something is found?
* Numerical loops with range
* Iterating a sliced list
* loops with list comprehension
* Explain while-else? When does the else condition set after the `while` statement fail to execute?
* Explain what does `continue` placed in a for loop do?
* Explain usage of enumerate, when can this be used

**See [tuples_basics.py](python-concepts/tuples_basics.py)**

* A tuple is an "unmodifiable" or "immutable" list
* List -> Tuple, Tuple -> List
* Slicing a tuple - How to skip count when slicing a tuple? 
* Can you slice a string?
* iterating a tuple
* Merge two lists - 2 techniques - using `+`, using extend() - recollect what is the difference in these two techniques
* Explain the use of `zip` data structure, when is it useful?

**See [dictionary_basics.py](python-concepts/dictionary_basics.py)**

* Using dictionaries
* Modifying value in a dictionary for one of the keys
* Deleting a key from a dictionary (3 ways). How to empty a dictionary?
* What is the difference between using square brackets to retrieve a value from a dictionary vs using `get()`
* Iterating dictionaries using `items()`, `keys()`, `values()`
* What is the default behaviour when neither of the 3 options above are qualified in a `for` loop explicitly, i.e., keys
  values are not specified in looping condition?
* Accessing elements from dictionaries
* How to convert a dictionary to kwargs?
* Printing kwargs, accessing individual elements in kwargs


**See [set_basics.py](python-concepts/set_basics.py)**

* What type of data can be added to set? (hint - hashable vs unhashable)
* Recollect methods for set operations
* Difference between remove and discard
* Union, Intersection and symmetric differences in sets

**See [conditional_basics.py](python-concepts/conditionals_basics.py)**

* learn `if-else-elif` pattern
* learn usage of `in` and `not in` pattern
* iterating through list using conditionals along the way


**Hashing concept in python [Hashing example](python-concepts/hashing.py)**

* What makes a data structure hashable?
* What is the real life use case to use a hashable data structure over a non-hashable data structure?

**See [user_inputs.py](python-concepts/user_inputs.py)**

* User inputs
* `while` loop - repeating user input until condition is not satisfied
* How to exit a `while` loop?
* Can you think of a way to populate a dictionary using user inputs?

**Function basics See - [functions_basics.py](python-concepts/functions_basics.py)**

* What are the 2 ways of passing arguments to functions? What is the default?
* In what order should default values be passed to a function? 
* How to pass keyword arguments to pass values to functions?
* Pitfalls of positional arguments?
* How to make a specific argument passed to a method as optional?
    - for e.g., - among first_name, middle_name, last_name how to make middle_name optional
* How to prevent a function from modifying an original copy of a `list` data structure?
* What is the significance of `/` and `*` when used in a function parameter?
* Why/when to define `*args` and `**kwargs` in a function parameter?

**Yield / Generator concept, see [Yield and Generators](python-concepts/yield_generators.py)**
* How does yield keyword work, what does it return?
* What is the exception type thrown by `yield` when the iteration ends ?

**Python Scopes - see [scopes.py](python-concepts/scopes.py)**
* What are the scopes in python, where a variable will be looked up to be resolved?
  * Hint: LEGB principle (Local -> Enclosed -> Global -> Built-ins)
* Functions can be declared in local scopes as well, they can access variables in both local and global scopes
* Global and nonlocal variables

**Programming paradigms**
- Imperative (procedural, structured, OOPS)
- Declarative (SQL style, Functional programming)

A pure function has only input and output - no side effects.
Haskell - purely functional - no loops

* Define Higher Order functions - [higher_order_functions.py](python-concepts/higher_order_functions.py):
- Function that takes another function as input
- Lambda functions, anonymous functions etc.,

* Explain the concept of currying from the perspective of functional programming, see [currying.py](python-concepts/currying.py)


**Python Modules See [restaurants.py](python-concepts/restaurants/restaurant.py)**

* Are there any restrictions in where the positional arguments or kwargs can be located in a function declaration?
  (hint: yes, at the end)
* Recollect the different ways to import modules and functions in python. How to import all the functions in a module?
* How does relative import work in python. Explain how to import `python-concepts/restaurants/restaurant.py` in
  another module `projects/tryit/ex1.py`
* What is the IDE setting if imports doesn't resolve (hint: Mark as sources root)


**Working with Classes, see - [Classes exercises](python-concepts/tryit)**

**See [Example with class instantiation and relative imports](python-concepts/relative_imports.py)**

* How does inheritance work in python?
* How to access variables in parent class in child class?
* How to import multiple classes from a module?
* How to import entire module?
* How does alias help in imports?

**Python Standard library**

* Example for `random` and using `randInt`, see [Random Dice](python-concepts/random_dice.py)
* Example for `random.sample`, see [Lottery analysis](python-concepts/lottery_analysis.py)
* Class naming conventions (hint: )

**Working With Files, see [Files Basics](python-concepts/reading_from_files)**

* How to open a file path and print contents?
* How to split a file to lines, then concatenate it without whitespace characters

**Exception Handling, see [exception basics](python-concepts/exception_basics.py)**

* What happens if a try-except block is not defined?
* How to execute a condition only if try block was successful?

**JSON Module, see [storing data basics](python-concepts/storing_data.py)**
* What is the difference between `json.dumps()` and `json.loads()`, when to use this?