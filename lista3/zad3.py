from functools import reduce
from sys import argv


def generator(filename):
    with open(filename, 'r') as file:
        return (int(line.split(' ')[-1]) for line in file.readlines())


def main():
    if len(argv) < 1:
        print("Give filename as argument")
        exit(0)

    print('Bytes :', sum(list(generator(argv[1]))))


if __name__ == '__main__':
    main()
