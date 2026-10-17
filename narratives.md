# HW2 — Question 1: TDD for Calc

- Language: Python 3.12, `unittest`
- Run tests: `python -m unittest CalcTest -v`
- AI usage: `Calc.py` and `CalcTest.py` were written by hand, without an AI coding agent. Claude Code 2.1.296 (model `claude-opus-5-5`) was used only to outline the assignment steps, review this narrative, and format it. See the AI usage log.

## Design Decisions Encoded in Tests

| Decision | Choice | Encoded in test |
|---|---|---|
| Return type of `divide` | `int` (integer division) | `test_divide`, `test_divide_return_int` |
| Rounding when the result is negative | Floor (toward negative infinity) | `test_negative_number_divide_round` |
| Division by zero | Raises `ZeroDivisionError` | `test_divide_by_zero` |

## TDD Cycles

### Cycle 1: `minus`

**Red: failing test**

```python
def test_minus(self):
    calc = Calculator()
    result = calc.minus(5, 3)
    self.assertEqual(result, 2)  # Expect 5 - 3 = 2
```

Failing output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ERROR

======================================================================
ERROR: test_minus (CalcTest.TestCalculator.test_minus)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../CalcTest.py", line 12, in test_minus
    result = calc.minus(5, 3)
             ^^^^^^^^^^
AttributeError: 'Calculator' object has no attribute 'minus'

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (errors=1)
```

Commit: `8ef1e7e test: add test for minus`

**Green: change to make it pass**

The test failed because `Calculator` had no `minus` method. I added `minus(a, b)`, which returns `a - b`. This is the smallest change that makes the test pass.

```python
def minus(self, a, b):
    return a - b
```

Passing output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Commit: `d6a1309 feat: add minus function to Calc`

**Refactor:** None needed. The method is a single expression.

---

### Cycle 2: `multiply`

**Red: failing test**

```python
def test_multiply(self):
    calc = Calculator()
    result = calc.multiply(2, 3)
    self.assertEqual(result, 6)  # Expect 2 * 3 = 6
```

Failing output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ok
test_multiply (CalcTest.TestCalculator.test_multiply) ... ERROR

======================================================================
ERROR: test_multiply (CalcTest.TestCalculator.test_multiply)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/atree/NYCU_COURSE/SW_test/HW2/CalcTest.py", line 17, in test_multiply
    result = calc.multiply(2, 3)
             ^^^^^^^^^^^^^
AttributeError: 'Calculator' object has no attribute 'multiply'

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (errors=1)
```

Commit: `cd9f0a7 test: add test for multiply`

**Green: change to make it pass**

I added `multiply(a, b)`, which returns `a * b`. This is the smallest change that makes the test pass.

```python
def multiply(self, a, b):
    return a * b
```

Passing output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ok
test_multiply (CalcTest.TestCalculator.test_multiply) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

Commit: `8471a15 feat: add multiply function to calc`

**Refactor:** None needed. The method is a single expression.

---

### Cycle 3: `divide`, basic behavior

This test sets the main design decision for `divide`: dividing two integers returns an integer, so `7 / 3` is expected to be `2`, not `2.333...`.

**Red: failing test**

```python
def test_divide(self):
    calc = Calculator()
    result = calc.divide(7, 3)
    self.assertEqual(result, 2)  # Expect 7 / 3 = 2
```

Failing output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_divide (CalcTest.TestCalculator.test_divide) ... ERROR
test_minus (CalcTest.TestCalculator.test_minus) ... ok
test_multiply (CalcTest.TestCalculator.test_multiply) ... ok

======================================================================
ERROR: test_divide (CalcTest.TestCalculator.test_divide)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/atree/NYCU_COURSE/SW_test/HW2/CalcTest.py", line 22, in test_divide
    result = calc.divide(7, 3)
             ^^^^^^^^^^^
AttributeError: 'Calculator' object has no attribute 'divide'

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (errors=1)
```

Commit: `dae2a6d test: add test for divide`

**Green: change to make it pass**

I added `divide(a, b)` using Python's floor division operator `//`, which returns an `int` when both operands are integers. Plain `/` would return `2.333...` and fail the test.

```python
def divide(self, a, b):
    return a // b
```

Passing output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_divide (CalcTest.TestCalculator.test_divide) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ok
test_multiply (CalcTest.TestCalculator.test_multiply) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

Commit: `2dcf543 feat: add function divide to calc`

**Refactor:** None needed. The method is a single expression.

---

### Cycle 4: `divide` by zero

> Note: This test passed on the first run, because Python's `//` operator already raises `ZeroDivisionError` when the divisor is 0. No implementation change was needed. The test records this decision, so a future change to `divide` cannot silently alter it.

**Test**

```python
def test_divide_by_zero(self):
    calc = Calculator()
    with self.assertRaises(ZeroDivisionError):
        calc.divide(5, 0)  # Expect division by zero to raise an error
```

Output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_divide (CalcTest.TestCalculator.test_divide) ... ok
test_divide_by_zero (CalcTest.TestCalculator.test_divide_by_zero) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ok
test_multiply (CalcTest.TestCalculator.test_multiply) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

Commit: `8ccfe2e test: add test for divided by zero`

---

### Cycle 5: Rounding when the result is negative

Integer division with a negative result can round in two ways:

- Floor (toward negative infinity), as Python does: `-7 // 3 == -3`
- Truncation (toward zero), as C and Java do: `-7 / 3 == -2`

I chose floor, and this test records that choice.

> Note: This test passed on the first run, because Python's `//` operator already rounds toward negative infinity. No implementation change was needed. If the choice had been truncation, the test would have failed and `divide` would have needed to change.

**Test**

```python
def test_negative_number_divide_round(self):
    calc = Calculator()
    result = calc.divide(-7, 3)
    self.assertEqual(result, -3)  # Expect -7 / 3 = -3 (floor division)
```

Output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_divide (CalcTest.TestCalculator.test_divide) ... ok
test_divide_by_zero (CalcTest.TestCalculator.test_divide_by_zero) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ok
test_multiply (CalcTest.TestCalculator.test_multiply) ... ok
test_negative_number_divide_round (CalcTest.TestCalculator.test_negative_number_divide_round) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

Commit: `756efd9 test: add test for rounding negative number`

---

### Cycle 6: `divide` returns an `int`

`test_divide` does not fully pin down the return type. In Python `2.0 == 2` is `True`, so an implementation that returns the float `2.0` would still pass `assertEqual(result, 2)`. This test checks the type directly.

> Note: This test passed on the first run, because `//` on two integers already returns an `int`. No implementation change was needed.

**Test**

```python
def test_divide_return_int(self):
    calc = Calculator()
    result = calc.divide(7, 3)
    self.assertIsInstance(result, int)  # Expect the result to be an integer
```

Output:

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_divide (CalcTest.TestCalculator.test_divide) ... ok
test_divide_by_zero (CalcTest.TestCalculator.test_divide_by_zero) ... ok
test_divide_return_int (CalcTest.TestCalculator.test_divide_return_int) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ok
test_multiply (CalcTest.TestCalculator.test_multiply) ... ok
test_negative_number_divide_round (CalcTest.TestCalculator.test_negative_number_divide_round) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Commit: `f54efff test: add test for divide returning int`

---

## Final Version of Calc

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a // b
```

## All Tests

```python
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
        self.assertIsInstance(result, int)  # Expect the result to be an integer

if __name__ == "__main__":
    unittest.main()
```

## Test Results

```text
❯ python -m unittest CalcTest -v
test_add (CalcTest.TestCalculator.test_add) ... ok
test_divide (CalcTest.TestCalculator.test_divide) ... ok
test_divide_by_zero (CalcTest.TestCalculator.test_divide_by_zero) ... ok
test_divide_return_int (CalcTest.TestCalculator.test_divide_return_int) ... ok
test_minus (CalcTest.TestCalculator.test_minus) ... ok
test_multiply (CalcTest.TestCalculator.test_multiply) ... ok
test_negative_number_divide_round (CalcTest.TestCalculator.test_negative_number_divide_round) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```

![All tests pass](screenshots/Q1_all_pass.png)

## Git Log

```text
f54efff (HEAD -> main) test: add test for divide returning int
756efd9 test: add test for rounding negative number
8ccfe2e test: add test for divided by zero
2dcf543 feat: add function divide to calc
dae2a6d test: add test for divide
8471a15 feat: add multiply function to calc
cd9f0a7 test: add test for multiply
d6a1309 feat: add minus function to Calc
8ef1e7e test: add test for minus
eeaa015 initial commit
```
