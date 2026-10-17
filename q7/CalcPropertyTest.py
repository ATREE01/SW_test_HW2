"""Property-based and metamorphic tests for Calc.

None of these tests hard-codes an expected value. Each one checks a relation
that must hold for every input, and Hypothesis generates the inputs.

The implementation under test is loaded from $CALC_DIR/Calc.py, so the same
tests can run against several implementations. CALC_DIR defaults to the HW2
directory, which holds the Calc from Questions 1 and 6.
"""
import importlib.util
import os
import unittest

from hypothesis import given, settings, strategies as st

# Hypothesis tries 100 random inputs per test by default. Set
# HYPOTHESIS_PROFILE=thorough to try 1000.
settings.register_profile("thorough", max_examples=1000)
settings.load_profile(os.environ.get("HYPOTHESIS_PROFILE", "default"))

HW2_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALC_DIR = os.environ.get("CALC_DIR", HW2_DIR)

_spec = importlib.util.spec_from_file_location(
    "Calc", os.path.join(CALC_DIR, "Calc.py"))
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
Calculator = _module.Calculator

ints = st.integers()
nonzero = st.integers().filter(lambda n: n != 0)


class TestCalculatorProperties(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # add / minus

    @given(ints, ints)
    def test_minus_undoes_add(self, a, b):
        c = self.calc
        self.assertEqual(c.minus(c.add(a, b), b), a)

    @given(ints, ints)
    def test_add_is_commutative(self, a, b):
        self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))

    @given(ints)
    def test_zero_is_identity_for_add(self, a):
        self.assertEqual(self.calc.add(a, 0), a)

    @given(ints)
    def test_minus_self_is_zero(self, a):
        self.assertEqual(self.calc.minus(a, a), 0)

    # multiply

    @given(ints, ints)
    def test_multiply_is_commutative(self, a, b):
        self.assertEqual(self.calc.multiply(a, b), self.calc.multiply(b, a))

    @given(ints)
    def test_one_is_identity_for_multiply(self, a):
        self.assertEqual(self.calc.multiply(a, 1), a)

    @given(ints, ints, ints)
    def test_multiply_distributes_over_add(self, a, b, c):
        calc = self.calc
        self.assertEqual(
            calc.multiply(a, calc.add(b, c)),
            calc.add(calc.multiply(a, b), calc.multiply(a, c)))

    # divide

    @given(ints, nonzero)
    def test_divide_returns_int(self, a, b):
        self.assertIsInstance(self.calc.divide(a, b), int)

    @given(ints, nonzero)
    def test_divide_matches_floor_division_definition(self, a, b):
        # Floor division: a == q * b + r, where r has the sign of b
        # and |r| < |b|.
        calc = self.calc
        q = calc.divide(a, b)
        r = calc.minus(a, calc.multiply(q, b))
        if b > 0:
            self.assertTrue(0 <= r < b, f"q={q}, r={r}")
        else:
            self.assertTrue(b < r <= 0, f"q={q}, r={r}")

    @given(ints, nonzero)
    def test_divide_undoes_multiply(self, a, b):
        calc = self.calc
        self.assertEqual(calc.divide(calc.multiply(a, b), b), a)

    @given(ints)
    def test_divide_by_zero_raises(self, a):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(a, 0)


if __name__ == "__main__":
    unittest.main()
