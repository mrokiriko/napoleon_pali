import unittest
from run import Tenet


class TddInPythonExample(unittest.TestCase):

    def bench(self, num, answer):
        guess = Tenet.is_palindrome(num)
        self.assertEqual(answer, guess)

    def test_basic_false(self):
        self.bench(123, False)

    def test_basic_true(self):
        self.bench(1221, True)

    def test_basic_true2(self):
        self.bench(313, True)

    def test_zero_problem(self):
        self.bench(314130, False)

    def test_same_digits(self):
        self.bench(111111111111111111111, True)

    def test_large(self):
        self.bench(123456789123456789123456789123456789987654321987654321987654321987654321, True)
