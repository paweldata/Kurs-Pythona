from functools import reduce
import datetime


def timer(function):
    def newFunction(*args, **kwargs):
        start = datetime.datetime.now()
        result = function(*args, **kwargs)
        end = datetime.datetime.now()

        diff = end - start
        print('Time in milliseconds :', diff.total_seconds() * 1000)

        return result
    return newFunction


@timer
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def main():
    print(factorial(10))


if __name__ == "__main__":
    main()
