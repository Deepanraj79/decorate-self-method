from module1 import AddSub
from module2 import MulDiv


def test_math1():
    """Method to run the log test of math operation in class AddSub """
    my_ins = AddSub()
    my_ins.add_num()
    my_ins.sub_num()


def test_math2():
    """Method to run the log test of math operation in class MulDiv """
    my_ins = MulDiv()
    my_ins.mul_num()
    my_ins.div_num()


if __name__ == "__main__":
    test_math1()
    test_math2()

