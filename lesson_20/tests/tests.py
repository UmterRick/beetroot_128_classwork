import math
import unittest
import datetime

import lesson_20.example as example


# import pytest


class AddFunctionTestCase(unittest.TestCase):

    def setUp(self):
        print("Set up test case env")
        self.x = 10
        self.time = datetime.datetime.now().time()
        self.pi = math.pi
        self.file = open("lesson_20/tests/tests.log", "r+")



    def test_add_1(self):
        if self.time.hour > 22:
            raise ValueError

        expected_result = self.x
        self.x = 100
        print("SET self.x = 100")
        actual_result = example.add(3, 7)
        self.assertEqual(expected_result, actual_result, )
        a = self.file.read()


    def test_add_2(self):
        expected_result = -self.x
        print(">>>>>", self.x)
        actual_result = example.add(-int(self.pi), -7)
        self.assertEqual(expected_result, actual_result)



    def test_add_3(self):
        expected_result = -10
        actual_result = example.add(-int(self.pi), -7)
        self.assertGreaterEqual(expected_result, actual_result)


    def tearDown(self):
        self.file.close()
        print("END OF TEST")