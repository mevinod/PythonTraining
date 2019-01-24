import unittest


class MyTest(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(10, add(10, 10))

    def testNeg(self):
        self.assertEqual(10, sub(10, 200))


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


unittest.main()
