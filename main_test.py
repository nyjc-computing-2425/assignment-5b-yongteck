import io
import sys

import unittest

class TestAssignment(unittest.TestCase):

    def test_str_raises_error(self):
        errmsg = "Unsupported input type"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        to_hms("10")
        sys.stdout = sys.__stdout__
        displaystr = capturedOutput.getvalue().strip()
        self.assertNotEqual(
            displaystr, "",
            msg="to_hms() does not display an error message when given a string"
         )
        self.assertTrue(
            displaystr.startswith(errmsg),
            msg="expected error message {errmsg!r}, got {displaystr!r}"
        )

    def test_value_7199(self):
        callstr = "to_hms(7199)"
        result = to_hms(7199)
        self.assertIsInstance(
            result, list,
            msg=f"{callstr} does not return a list of three integers"
        )
        self.assertEqual(
            len(result), 3,
            msg=f"{callstr} does not return a list of three integers"
        )
        for i in range(3):
            self.assertIsInstance(
                result[i], int,
                msg=f"{callstr} does not return a list of three integers"
            )
        self.assertCountEqual(
            result, [1, 59, 59],
        )

    def test_value_61(self):
        callstr = "to_hms(61)"
        result = to_hms(61)
        self.assertIsInstance(
            result, list,
            msg=f"{callstr} does not return a list of three integers"
        )
        self.assertEqual(
            len(result), 3,
            msg=f"{callstr} does not return a list of three integers"
        )
        for i in range(3):
            self.assertIsInstance(
                result[i], int,
                msg=f"{callstr} does not return a list of three integers"
            )
        self.assertCountEqual(
            result, [0, 1, 1],
        )

    def test_value_10(self):
        callstr = "to_hms(10)"
        result = to_hms(10)
        self.assertIsInstance(
            result, list,
            msg=f"{callstr} does not return a list of three integers"
        )
        self.assertEqual(
            len(result), 3,
            msg=f"{callstr} does not return a list of three integers"
        )
        for i in range(3):
            self.assertIsInstance(
                result[i], int,
                msg=f"{callstr} does not return a list of three integers"
            )
        self.assertCountEqual(
            result, [0, 0, 10]
        )

    def test_docstrings(self):
    for func in [to_hms]:
        self.assertIs(hasattr(func, "__doc__"), True)
        self.assertTrue(func.__doc__, f"{func.__name__}() does not have a docstring")


if __name__ == '__main__':
    unittest.main()
