# coding= utf-8


class Calculator:
    def __init__(self, input_a, input_b):
        self._input_a = input_a
        self._input_b = input_b
        self._output = 0.0

    def is_valid_number(self):
        """
        check if values are valid types
        return: bool
        """
        if isinstance(self._input_a, int) or isinstance(self._input_a, float):
            self._input_a = float(self._input_a)
            return True
        elif isinstance(self._input_b, int) or isinstance(self._input_b, float):
            self._input_b = float(self._input_b)
            return True
        return False

    def add(self):
        if not self.is_valid_number():
            return False
        self._output = self._input_a + self._input_b
        return True

    def subtract(self):
        if not self.is_valid_number():
            return False
        self._output = self._input_a - self._input_b
        if self._output < 0.0:
            self._output = self._input_b - self._input_a
        return True

    def multiple(self):
        if not self.is_valid_number():
            return False
        self._output = self._input_a * self._input_b
        return True

    def divide(self):
        if not self.is_valid_number():
            return False
        self._output = self._input_a / self._input_b
        return True

    def modulo(self):
        if not self.is_valid_number():
            return False
        self._output = self._input_a % self._input_b
        return True

    def get_output(self):
        return self._output

    def set_input_a(self, input_a):
        self._input_a = input_a

    def set_input_b(self, input_b):
        self._input_b = input_b