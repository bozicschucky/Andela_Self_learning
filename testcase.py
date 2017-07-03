import unittest
from primenumbers import prime_numbers

class PrimeNumber_Tests(unittest.TestCase):

        def test_number_output(self):
            self.assertEqual(set([2, 3, 5]), prime_numbers(5))

        def test_number_output1(self):
            self.assertEqual(set([2]), prime_numbers(2))

        def test_number_output2(self):
            self.assertEqual(set([2, 3]), prime_numbers(3))

        def test_number_output3(self):
            self.assertEqual(set([2, 3, 5, 7]), prime_numbers(7))

        def test_positive_number(self):
            self.assertTrue(set(prime_numbers(6)) > 0)

if __name__ == '__main__':
    unittest.main()
