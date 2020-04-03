from inspect import getfullargspec
from math import sqrt


class overloadClass:
    functions = {}

    def __init__(self, fn):
        self.__name = fn.__name__
        overloadClass.functions[tuple([fn.__name__] + getfullargspec(fn).args)] = fn

    def __call__(self, *args, **kwargs):
        for key in overloadClass.functions:
            if self.__name == key[0] and len(key) - 1 == len(args):
                return overloadClass.functions[key](*args, **kwargs)


def overload(function):
    return overloadClass(function)


@overload
def norm(x, y):
    return sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


@overload
def myPrint(a):
    print(a)


@overload
def myPrint(a, b):
    print(a, b)


def main():
    print(f"norm(2,4) = {norm(2, 4)}")
    print(f"norm(2,3,4) = {norm(2, 3, 4)}")
    myPrint("Is it work?")
    myPrint("Yes,", "it works")


if __name__ == '__main__':
    main()
