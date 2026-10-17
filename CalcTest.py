import unittest
from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_minus(self):
        calc = Calculator()
        result = calc.minus(5, 3)
        self.assertEqual(result, 2)  # Expect 5 - 3 = 2

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(2, 3)
        self.assertEqual(result, 6)  # Expect 2 * 3 = 6

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(7, 3)
        self.assertEqual(result, 2)  # Expect 7 / 3 = 2

    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)  # Expect division by zero to raise an error

    def test_negative_number_divide_round(self):
        calc = Calculator()
        result = calc.divide(-7, 3)
        self.assertEqual(result, -3)  # Expect -7 / 3 = -3 (floor division)

    def test_divide_return_int(self):
        calc = Calculator()
        result = calc.divide(7, 3)
        self.assertIsInstance(result, int)  # Expect the result to be an int

    def test_modulo(self):
        calc = Calculator()
        result = calc.modulo(7, 3)
        self.assertEqual(result, 1)  # Expect 7 % 3 = 1

    def test_modulo_negative_operand(self):
        calc = Calculator()
        result = calc.modulo(-7, 3)
        self.assertEqual(result, 2)  # Expect -7 % 3 = 2 (sign of divisor)

    def test_modulo_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.modulo(5, 0)  # Expect modulo by zero to raise an error

    def test_power(self):
        calc = Calculator()
        result = calc.power(2, 3)
        self.assertEqual(result, 8)  # Expect 2 ** 3 = 8

    def test_power_zero_to_zero(self):
        calc = Calculator()
        result = calc.power(0, 0)
        self.assertEqual(result, 1)  # Expect 0 ** 0 = 1

    def test_power_negative_exponent(self):
        calc = Calculator()
        result = calc.power(2, -1)
        self.assertEqual(result, 0.5)  # Expect 2 ** -1 = 0.5 (a float)


if __name__ == "__main__":
    unittest.main()
