"""Logger Initialization

References of creating Logger class following the singleton pattern:

https://gist.github.com/huklee/cea20761dd05da7c39120084f52fcc7c
https://www.semicolonworld.com/question/42958/creating-a-singleton-in-python
"""
import os
import datetime
import logging
import functools


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyLogger(metaclass=SingletonType):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s | %(filename)s:%(lineno)s] %(message)s'
        )

        # now = datetime.datetime.now()
        # dir_name = "./log"
        # if not os.path.isdir(dir_name):
        #     os.mkdir(dir_name)
        # file_handler = logging.FileHandler(dir_name + "/log_" + now.strftime("%Y-%m-%d")+".log")
        # file_handler.setFormatter(formatter)
        # self._logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

        self._logger.info("Logger initialization done")

    def get_logger(self):
        return self._logger


class Logger:

    logger = MyLogger.__call__().get_logger()


def track_function_state(source_func):
    @functools.wraps(source_func)
    def wrapper(self, *args, **kwargs):
        function_name = source_func.__name__
        self.logger.debug(f"{function_name} - starts")
        ret = source_func(self, *args, **kwargs)
        self.logger.debug(f"{function_name} - ends")
        return ret

    return wrapper