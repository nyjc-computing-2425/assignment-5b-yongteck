import io
import csv
import os
import sys
import unittest

from main import *

class TestAssignment(unittest.TestCase):

    def test_part1(self):
        filename = "pre-u-enrolment-by-age.csv"
        header, data = read_csv(filename)
        for label in header:
            self.assertIsInstance(
            label, str,
            msg="header should be a list of four strs"
        )
        for i, row in enumerate(data, start=1):
            self.assertIsInstance(
                row, list,
                msg="data should be a list of rows, each row represented by a list"
            )
            self.assertIsInstance(
                row[0], int,
                msg=f"First item in row {i} should be an int"
            )
            self.assertIsInstance(
                row[1], str,
                msg=f"Second item in row {i} should be a str"
            )
            self.assertIsInstance(
                row[2], str,
                msg=f"Third item in row {i} should be a str"
            )
            self.assertIsInstance(
                row[3], int,
                msg=f"Fourth item in row {i} should be an int"
            )

    def test_part2(self):
        filename = "pre-u-enrolment-by-age.csv"
        header, enrolment = read_csv(filename)
        mf_enrolment = filter_gender(enrolment, "MF")
        for i, row in enumerate(mf_enrolment, start=1):
            self.assertEqual(
                len(row), 3,
                msg="After filtering, each row (list) should have only three items"
            )
            self.assertIsInstance(
                row[0], int,
                msg=f"First item in row {i} should be an int"
            )
            self.assertIsInstance(
                row[1], str,
                msg=f"Second item in row {i} should be a str"
            )
            self.assertIsInstance(
                row[2], int,
                msg=f"Third item in row {i} should be an int"
            )

    def test_part3(self):
        filename = "pre-u-enrolment-by-age.csv"
        header, enrolment = read_csv(filename)
        mf_enrolment = filter_gender(enrolment, "MF")
        enrolment_by_year = sum_by_year(mf_enrolment)
        for i, row in enumerate(enrolment_by_year, start=1):
            self.assertEqual(
                len(row), 2,
                msg="After summing, each row should only have two items"
            )
            year, total = row
            self.assertIsInstance(
                year, int,
                msg=f"First item of row {i} should be an int"
            )
            self.assertIsInstance(
                total, int,
                msg=f"First item of row {i} should be an int"
            )

    def test_part4(self):
        correct_enrolment = {
            1984: 21471, 1985: 24699, 1986: 27598, 1987: 29508, 1988: 32082, 1989: 31729,
            1990: 29214, 1991: 27224, 1992: 24663, 1993: 23958, 1994: 22857, 1995: 21690,
            1996: 21858, 1997: 22311, 1998: 23530, 1999: 24834, 2000: 24804, 2001: 24376,
            2002: 25376, 2003: 24559, 2004: 24681, 2005: 28901, 2006: 30726, 2007: 31627,
            2008: 32579, 2009: 32110, 2010: 32420, 2011: 32296, 2012: 32087, 2013: 32165,
            2014: 31613, 2015: 29559, 2016: 28442, 2017: 29252, 2018: 29012,
        }
        filename = "pre-u-enrolment-by-age.csv"
        header, enrolment = read_csv(filename)
        mf_enrolment = filter_gender(enrolment, "MF")
        enrolment_by_year = sum_by_year(mf_enrolment)
        header = ["year", "total_enrolment"]
        outfile = "total-enrolment-by-year.csv"
        write_csv(outfile, header, enrolment_by_year)
        with open(outfile, 'r') as f:
            for record in csv.DictReader(f):
                self.assertTrue(record["year"].isdecimal(), "year has non-decimal characters! eg. spacing")
                self.assertTrue(record["total_enrolment"].isdecimal(), "total_enrolment has non-decimal characters! eg. spacing")
                year, total_enrolment = int(record["year"]), int(record["total_enrolment"])
                self.assertEqual(
                    total_enrolment, correct_enrolment[year],
                    msg=f"Correct enrolment for {year} should be {correct_enrolment[year]}, got {total_enrolment} instead"
                )
        try:
            os.remove(outfile)
        except Exception:
            pass

    def test_docstrings(self):
        for func in [read_csv, filter_gender, sum_by_year, write_csv]:
            self.assertIs(hasattr(func, "__doc__"), True)
            self.assertTrue(func.__doc__, f"{func.__name__}() does not have a docstring")


if __name__ == '__main__':
    import os
    if not os.listdir("autograding"):
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
    unittest.main()
