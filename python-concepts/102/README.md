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
* Recollect Set mathematical operations (union, intersection, difference, symmetric difference),
  see [Set Math](practice/mathematical_set_operations.py)

## Data Visualization

* What are the basic stat functions in python (mean, median, mode, sum, count,
  range) [Stat functions](practice/numpy_stat_functions.py)
* How can you chart a barplot for a six-sided dice roll ?
  See - [Static Visualizations](practice/static_visualizations.py)

### Data visualization python libraries

- seaborn
- matplotlib

## Python and datascience

### Basics

- sum
- count
- range
- minimum
- maximum

### Beyond basics

- mean
- median
- mode : Most frequent occurrence

Dispersion - Defines spread of given numbers how closer or distant they are
Standard deviation: sqrt of variance

## Numpy

* Numeric python - most two-dimensional array in python always use numpy
* Pandas library is based on numpy

Numpy has a high performance array called as `ndarray` that is 35% more performant than the list array data structure
in python.

### ndarray basics

**See [numpy_ndarray](practice/numpy_ndarray.py)**

* How to find out the datatype of a numpy array?
* What are dimensions in ndarray?
* What are shape attribute in ndarray?
* What is the difference between `size` and `itemsize` in a `ndarray`?
* How to flatten a ndarray? What is the difference between `flatten()` and `.flat` attribute?
* Explain the `arange` function? How similar or different is it from `range`?
* How to generate floating point array ranges using numpy?
* What is the purpose of `reshape` in numpy?
* How does array broadcasting work in numpy?
* What is the use of `linspace` function in numpy?

### Numpy calculation methods

* Does numpy have built-in values for stats? [Numpy stats](practice/numpy_stats.py)
* How to find average by row or column using numpy?
* What are universal functions in python, how to use them? [Numpy universal functions](practice/universal_functions.py)

### Numpy array operations

See - [Numpy Array Operations](practice/numpy_array_ops.py)

* How to choose to find specific rows in ndarray?
* How to find specific columns in ndarray?
* How to slice data from ndarray?
* How to transpose an `ndarray`?
* How does array horizontal stack and vertical stacking work?

### Numpy object references

See - [Numpy References](practice/numpy_references.py)

* What is the difference between `copy` and `view` in numpy?
* How does `deepcopy` work?
* What is the difference between `flatten` and `ravel`?

