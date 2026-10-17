class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # Floor division: rounds toward negative infinity (-7 // 3 == -3);
        # raises ZeroDivisionError when b == 0.
        return a // b
