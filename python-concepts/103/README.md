# Python 103 README

- [Format Specification Review for Strings](practice/format_specification_review.py)
- [String Review](practice/strings_review.py)
- [Regular Expressions](practice/regex_review.py)

## Recollection questions

See - [Strings Review](practice/strings_review.py)

* How to `partition` a string? when is this useful? What's the difference of `partition` from a `split`?
* What is the use of `reversed` keyword on a list?
* How to append a comma after every element of the number "0 1 2 4 5"?
* What are character testing methods in string class?
* How to format a money value with comma?

## Regex questions

See - [Regex Practice](practice/regex_review.py)

- How to use the `re` module in python, what are the commonly used functions?
- How to find exact match?
- What is the difference between `search` and `match` functions?
- What are the regex meta-character classes?
- How to perform substitution actions using regex functions? How to make it selective?
- Can regex module be used to search case-insensitive? What's given along with the search expression to achieve this?
- Why is `findall` used?
- What is the difference between `findall` and `finditer`
- how to capture subgroups in regex?

## Data munging with Pandas

See - [Pandas RegEx](practice/pandas_regex.py)

- data munging = data cleaning
- Two common operations: data cleaning, data transformation
- Can RegEx be used in pandas Series? What is the difference between `match` and `contains`?
- How to apply regex on dataframes to replace a column with different format?

## File processing

see - [Files Review](practice/files_review.py)

- What is the use of `with` statement in resource management? Can it only be used with files?
- How to create a new file and append data in python?
- What is the use of `sys` module in python?
- How to remove a file in python from disk? On the same line, how to rename a file?
- what is the difference using `readlines` in python vs using an iterator to read one line at a time?
- What is the difference using `split(" ")` vs `split()` default while splitting a line?
- What are the file open modes in python ? (Hint - There are six of them)

## JSON module

See - [JSON Review](practice/json_review.py)

- What is the difference between `json.dump()` and `json.dumps()` method?
- What is the use of `json.load`? 
- How to pretty-print contents of a file containing json objects?


## CSV files

* `csv` module is used, many libraries also support CSV processing
* How to read and write to csv using this module?
* How to create csv from pandas dataframes, how to read a csv file into pandas dataframe?