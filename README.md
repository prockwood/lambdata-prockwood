# lambdata-prockwood

## A collection of useful(?) functions for transformation or info-getting from pandas DataFrames and Series'

## Functions include:
- _null_count()_, which counts total null values in a DataFrame.
- _train_test_split()_, a basic re-implementation of sklearn's iconic function.
- _randomize()_, which shuffles the elements of a DataFrame on both axis.
- _addy_split()_, which turns a Series of street addresses strings into a nice DataFrame with information broken-out into columns.
- _check_elements_eq()_, which checks the equivalence of two DataFrames elements, element by element, and supports the comparison of null types which pandas.DataFrame.equals() does not. So, so there.

## Installation
Just clone this repo silly!
```sh
git clone https://github.com/prockwood/lambdata_prockwood
```

### Licence
[MIT](LICENSE)
