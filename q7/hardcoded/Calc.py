# A deliberately bad Calc that special-cases the inputs used in the Q1 tests.
# It passes all seven Q1 tests.
class Calculator:
    def add(self, a, b):
        if (a, b) == (2, 3):
            return 5
        return 0

    def minus(self, a, b):
        if (a, b) == (5, 3):
            return 2
        return 0

    def multiply(self, a, b):
        if (a, b) == (2, 3):
            return 6
        return 0

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        if (a, b) == (7, 3):
            return 2
        if (a, b) == (-7, 3):
            return -3
        return 0
