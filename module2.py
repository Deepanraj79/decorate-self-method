"""Module to perform the basic mathematical operation, Multiplication and Division
of two numbers.
"""

from log import Logger, track_function_state


class MulDiv(Logger):

    def __init__(self, arg1=1, arg2=3):
        self.arg1 = arg1
        self.arg2 = arg2

    @track_function_state
    def mul_num(self):
        """Multiplication of two numbers"""
        self.logger.info(f'Addition: {self.arg1 * self.arg2}')

    @track_function_state
    def div_num(self):
        """Division of two numbers"""
        self.logger.info(f'Subtraction: {self.arg1 * self.arg2}')

