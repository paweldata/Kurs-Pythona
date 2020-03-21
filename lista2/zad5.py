from random import SystemRandom
from random import getrandbits
from math import gcd
import sys


# Miller–Rabin primality test
def isPrime(number):
    systemRandom = SystemRandom()

    if number == 2:
        return True
    if number < 1 or number % 2 == 0:
        return False
    s = 0
    d = number - 1

    while d % 2 == 0:
        d //= 2
        s = s + 1

    for _ in range(128):
        x = systemRandom.randint(2, number - 1)
        x = pow(x, d, number)
        if x != 1 and x != number - 1:
            for i in range(s):
                x = pow(x, 2, number)
                if x == 1:
                    return False
                if x == number - 1:
                    break
            if x != number - 1:
                return False
    return True


def generatePrime(length):
    prime = 0
    while not isPrime(prime):
        prime = getrandbits(length)
        prime |= (1 << length - 1) | 1
    return prime


def modularMultiplicativeInverse(number, mod):
    # ax + by = 1
    modSave = mod
    y = 0
    x = 1

    while number > 1:
        q = number // mod
        t = mod

        mod = number % mod
        number = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        return x + modSave
    return x


def generateKeys(length):
    systemRandom = SystemRandom()

    prime1 = generatePrime(length)
    prime2 = generatePrime(length)
    number = (prime1 - 1) * (prime2 - 1)

    e = systemRandom.randint(1, number)
    while gcd(number, e) != 1:
        e = systemRandom.randint(1, number)

    d = modularMultiplicativeInverse(e, number)

    with open("key.pub", 'w') as file:
        file.write(str(prime1 * prime2) + ' ' + str(e))

    with open("key.prv", 'w') as file:
        file.write(str(prime1 * prime2) + ' ' + str(d))


def encrypt(string, number, key):
    length = len(bin(int(number))[2::]) - 1

    # convert to binary string
    binaryCode = ''.join('{0:08b}'.format(ord(char), 'b') for char in string)

    # split to parts with length <  number
    binaryCode = [binaryCode[i: i + length] for i in range(0, len(binaryCode), length)]

    return ' '.join(str(pow(int(code, 2), int(key), int(number))) for code in binaryCode)


def decrypt(string, number, key):
    length = len(bin(int(number))[2::]) - 1
    binaryCode = [str(bin(pow(int(code), int(key), int(number)))[2::]) for code in string.split(' ')]

    # add char '0'
    for i, code in enumerate(binaryCode):
        if i < len(binaryCode) - 1:
            binaryCode[i] = '0' * (length - len(code)) + code

    # add char '0' to last part
    if sum(len(code) for code in binaryCode) % 8 > 0:
        binaryCode[-1] = '0' * (8 - (sum(len(code) for code in binaryCode) % 8)) + binaryCode[-1]

    binaryCode = ''.join(binaryCode)

    return ''.join(chr(int(binaryCode[i: i + 8], 2)) for i in range(0, len(binaryCode), 8))


def errorInfo():
    print('Give arguments:\n'
          '--gen-keys number_of_bits\nor\n'
          '--encrypt code\nor\n'
          '--decrypt code\n')


def main():
    if len(sys.argv) < 3:
        errorInfo()
        exit()

    elif sys.argv[1] == '--gen-keys':
        generateKeys(int(sys.argv[2]))
    elif sys.argv[1] == '--encrypt':
        try:
            with open('key.pub', 'r') as file:
                number, key = file.read().split(' ')
            print(encrypt(' '.join([string for i, string in enumerate(sys.argv) if i >= 2]), number, key))
        except IOError:
            print("File key.pub not exists")
    elif sys.argv[1] == '--decrypt':
        try:
            with open('key.prv', 'r') as file:
                number, key = file.read().split(' ')
            print(decrypt(' '.join([string for i, string in enumerate(sys.argv) if i >= 2]), number, key))
        except IOError:
            print("File key.prv not exists")
    else:
        errorInfo()


if __name__ == '__main__':
    main()
