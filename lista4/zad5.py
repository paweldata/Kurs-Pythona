from math import pi
from cmath import exp
from sys import argv


class FastBigNum:
    def __init__(self, number):
        self.__value = int(number)

    def __str__(self):
        return str(self.__value)

    def __DFT(self, number):
        size = len(number)
        answer = [0] * size

        for i in range(size):
            for k in range(size):
                answer[i] += int(number[k]) * exp(- 2j * pi * i * k / size)

        return answer

    def __DFTInverse(self, number):
        size = len(number)
        answer = [0] * size

        for i in range(size):
            for j in range(size):
                answer[i] += number[j] * exp(1j * pi * 2 * i * j / size)
            answer[i] = int(round(answer[i].real / size))

        return answer

    def __mul__(self, other):
        size = len(str(self.__value)) + len(str(other))
        
        dft1 = self.__DFT(str(self.__value)[::-1] + '0' * (size - len(str(self.__value))))
        dft2 = self.__DFT(str(other)[::-1] + '0' * (size - len(str(other))))

        answer = [a * b for a, b in zip(dft1, dft2)]
        answer = answer + [0] * (size - len(answer))
        answer = self.__DFTInverse(answer)

        return FastBigNum(sum(answer[i] * 10 ** i for i in range(len(answer))))


def main():
    if len(argv) < 3:
        print("Give 2 numbers as argument\n")
        return 0

    a = FastBigNum(argv[1])
    b = FastBigNum(argv[2])
    result = a*b
    print(result)

    if str(result) == str(int(argv[1]) * int(argv[2])):
        print('It works')
    else:
        print("It doesn't work :/")


if __name__ == '__main__':
    main()
