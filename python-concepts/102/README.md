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

Recollect:
* What is the difference between list comprehensions and generator expressions?
* How to perform case-insensitive compare in strings? (hint: str.casefold())
* How can you chart a barplot for a six-sided dice roll ? See - [Static Visualizations](static_visualizations.py)
* 