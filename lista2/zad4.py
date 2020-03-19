import os.path
import sys
import hashlib


def findDuplicates(path):
    codeMap = {}

    for root, dirs, files in os.walk(path):
        for file in files:
            filename = os.path.join(root, file)

            with open(filename, 'rb') as f:
                code = hashlib.md5(f.read()).hexdigest() + ' ' + str(os.path.getsize(filename))
                if code not in codeMap:
                    codeMap[code] = []
                codeMap[code].append(filename)

    for code in codeMap:
        if len(codeMap[code]) > 1:
            for filename in codeMap[code]:
                print(filename)
            print('----------')


def main():
    if len(sys.argv) < 2:
        print("Give folder as argument")
    else:
        findDuplicates(sys.argv[1])


if __name__ == '__main__':
    main()
