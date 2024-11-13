import unittest

from lesson_20 import example


class DivideFunctionTestCase(unittest.TestCase):

    def test_divide_1(self):
        expected_result = 2
        actual_result = example.divide(14, 7)
        self.assertEqual(expected_result, actual_result, )

    def test_divide_2(self):
        expected_result = -20
        actual_result = example.divide(-100, 5)
        self.assertEqual(expected_result, actual_result)


class DivideFunctionTestCase_2(unittest.TestCase):

    def test_divide_1(self):
        expected_result = 2
        actual_result = example.divide(14, 7)
        self.assertEqual(expected_result, actual_result, )

    def test_divide_2(self):
        expected_result = -20
        actual_result = example.divide(-100, 5)
        self.assertEqual(expected_result, actual_result)
