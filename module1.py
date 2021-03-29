"""Module to perform the basic mathematical operation, Addition and Subtraction
of two numbers.
"""
from log import Logger, track_function_state


class AddSub(Logger):

    def __init__(self, arg1=5, arg2=3):
        self.arg1 = arg1
        self.arg2 = arg2

    @track_function_state
    def add_num(self):
        """Addition of two numbers"""
        self.logger.info(f'ADD: {self.arg1 + self.arg2}')

    @track_function_state
    def sub_num(self):
        """Subtraction of two numbers"""
        self.logger.info(f'ADD: {self.arg2 - self.arg2}')


