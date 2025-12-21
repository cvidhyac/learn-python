# Python 102 README

## Using poetry

`poetry env use $(pyenv which python)`

`poetry add matplotlib seaborn`

`poetry run jupyter lab`

## Higher order functions

* The basic statistical functions like `mean`, `median`, `mode`, `sum`, `count` are all types of "reduce"
functions because they accept an iterable and return a single value in response
* Lambda functions in python are only expression lambda, unlike java it does not support statement lambda.
* map, filter, reduce - similar to how these concepts are used in Java, they return an iterator

## Review - Dictionaries and Sets
* What is the difference between list comprehensions and generator expressions?
* How to perform case-insensitive compare in strings? (hint: str.casefold())
* Recollect how dictionary comprehension works? see - [Dictionary comprehension](practice/dictionary_comprehensions.py)
* How to represent an empty set, why we can't represent an empty set like `{}` similar to how we could represent 
an empty list using `[]`
* [Dictionary comprehensions](practice/dictionary_comprehensions.py)
* Recollect Set mathematical operations (union, intersection, difference, symmetric difference), see [Set Math](practice/mathematical_set_operations.py)

## Data Visualization 
* What are the basic stat functions in python (mean, median, mode, sum, count, range) [Stat functions](practice/stat_functions.py)
* How can you chart a barplot for a six-sided dice roll ? See - [Static Visualizations](practice/static_visualizations.py)