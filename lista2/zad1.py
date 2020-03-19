import sys
import os


def main():
    if len(sys.argv) < 2:
        print("Give filename as argument")
        exit()

    with open(sys.argv[1], 'r') as file:
        text = file.read()
        print('Bytes : ', os.path.getsize(sys.argv[1]))
        print('Words : ', len(text.split()))
        lines = text.split('\n')
        print('Lines : ', len(lines) - 1)
        print('Max line : ', max(len(line) for line in lines))


if __name__ == '__main__':
    main()
