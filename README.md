In this assignment, you should write your code in a **readable** way.

Your function definitions should have **appropriate docstrings**.

# Assignment 5b: Comma-separated values (CSV)

The file `pre-u-enrolment-by-age.csv` contains data on pre-university enrolment numbers, sorted by year, age, and gender.

## Part 1: Read data from a CSV file and edit it

Define a **function**, `read_csv(filename)`, that:

1. Takes a string `filename`
2. Reads CSV data stored in `filename`
3. Returns two values, `(header, data)`:
   - `header` is a **list** containing the column labels (from the first row)
   - `data` is a **nested list** containing the data.

Data should be converted to appropriate types, i.e. `int`, `float`, or `str`.

----------

## Part 2: Filter the data

Define a function `filter_gender(enrolment_by_age, sex)` that:

1. Takes a list of records `enrolment_by_age` and a string `sex`
2. Return a list of records where the value in the "sex" column matches string `sex`  
(We are only keeping data for total enrolment, not split by gender.)
3. Exclude the `sex` column from the returned records.

You should end up with data for three columns: `year`, `age`, and `enrolment_jc`.

### Sample output: new_data

    >>> mf_enrolment = filter_gender(enrolment_data, "MF")
    >>> mf_enrolment
    [[1984, '17 YRS', 8710],
     [1984, '18 YRS', 3927],
     [...],
     [...],
     ...]

You may use the header indexes directly.

## Part 3: Sum up enrolment by year

Define a function, `sum_by_year(enrolment_data)`, that will:

1. Add up the total enrolment for each year, regardless of age
2. Return the result as a list of lists. Each inner list comprises two integers, `year` and `total_enrolment`.

You may assume that the last item in the record is the enrolment.

### Sample output: enrolment_by_year

    >>> enrolment_by_year = sum_by_year(mf_enrolment)
    >>> enrolment_by_year
    [[1984, 21471],
     [1985, 24699],
     [...],
     [...],
     ...]

## Task 4: Write the data to a CSV file

Define a function, `write_csv(filename, header, data)`, that will write `header` and `data` to `filename` in CSV format and return the number of lines written. Any existing data in `filename` should be ignored and overwritten.

Write your data to a CSV file, `total-enrolment-by-year.csv`, in the same format as the original file.

### Sample output

    >>> filename = 'total-enrolment-by-year.csv'
    >>> header = ["year", "total_enrolment"]
    >>> write_csv(filename, header, enrolment_by_year)
    35

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.

