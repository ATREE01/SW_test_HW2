# A plausible-looking Calc that floors a float quotient instead of using //.
# It passes all seven Q1 tests, but the float division loses precision for
# large integers.
import math


class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return math.floor(a / b)
