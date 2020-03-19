import os.path
import sys


def toLower(path, filename):
    directory = os.path.join(path, filename)
    if os.path.isdir(directory):
        for file in os.listdir(directory):
            toLower(directory, file)

    os.rename(directory, os.path.join(path, filename.lower()))


def main():
    if len(sys.argv) < 2:
        print("Give folder as argument")
    else:
        toLower(sys.argv[1], '')


if __name__ == '__main__':
    main()
