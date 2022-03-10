import unittest

from calculator import division, multiplication, subtract, sum

# # Testa soma de dois números inteiros
# if sum(2, 4) == 6:
#     print('Success')
# else:
#     print('Fail')

# # Testa somas com zero
# if sum(2, 0) == 2:
#     print('Success')
# else:
#     print('Fail')


class TestSum(unittest.TestCase):
    def test_som_two_integer_numbers(self):
        self.assertEqual(sum(4, 3), 7)

    def test_som_number_with_zero(self):
        self.assertEqual(sum(0, 4), 4)

    def test_som_with_negative_number(self):
        self.assertEqual(sum(8, -2), 6)


class TestDivision(unittest.TestCase):
    def test_dividing_number_by_one_returns_the_number(self):
        self.assertEqual(division(7, 1), 7)

    def test_dividing_number_by_zero(self):
        self.assertEqual(division(10, 0), 'Não é um número')


class TestSubtration(unittest.TestCase):
    def test_subtration_negative_number(self):
        self.assertEqual(subtract(4, -3), 7)

    def test_subtration_by_zero(self):
        self.assertEqual(subtract(4, 0), 4)

    def test_subtration_by_number(self):
        self.assertEqual(subtract(4, 7), -3)


class TestMultiplication(unittest.TestCase):
    def test_multiplicate_by_zero(self):
        self.assertEqual(multiplication(6, 0), 0)

    def test_multiplicate_by_one(self):
        self.assertEqual(multiplication(6, 1), 6)

    def test_multiplicate_numbers(self):
        self.assertEqual(multiplication(4, 3), 12)


unittest.main()
