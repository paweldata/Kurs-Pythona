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


def encrypt(string):
    with open('key.pub', 'r') as file:
        number, key = file.read().split(' ')

    binaryCode = ''.join('{0:08b}'.format(ord(char), 'b') for char in string)
    return pow(int(binaryCode, 2), int(key), int(number))


def decrypt(string):
    with open('key.prv', 'r') as file:
        number, key = file.read().split(' ')

    binaryCode = pow(int(string), int(key), int(number))
    binaryCode = str(bin(binaryCode))[2::]
    if len(binaryCode) % 8 != 0:
        binaryCode = '0' * (8 - (len(binaryCode) % 8)) + binaryCode

    answer = ''
    for i in range(0, len(binaryCode), 8):
        answer += chr(int(binaryCode[i: i + 8], 2))

    return answer


def errorInfo():
    print('Give arguments:\n'
          '--gen-keys number_of_bits\nor\n'
          '--encrypt code\nor\n'
          '--decrypt code\n')


def main():
    if len(sys.argv) < 3:
        errorInfo()
        exit()

    if sys.argv[1] == '--gen-keys':
        generateKeys(int(sys.argv[2]))
    elif sys.argv[1] == '--encrypt':
        print(encrypt(sys.argv[2]))
    elif sys.argv[1] == '--decrypt':
        print(decrypt(sys.argv[2]))
    else:
        errorInfo()


if __name__ == '__main__':
    main()
