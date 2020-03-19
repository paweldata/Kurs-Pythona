import sys

table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(string):
    binaryCode = ''.join('{0:08b}'.format(ord(char), 'b') for char in string)
    answer = ''

    if len(binaryCode) % 6 != 0:
        binaryCode += '0' * (6 - (len(binaryCode) % 6))

    for i in range(0, len(binaryCode), 6):
        answer += table[int(binaryCode[i: i + 6], 2)]

    if len(answer) % 4 != 0:
        answer += '=' * (4 - (len(answer) % 4))

    return answer


def decode(string):
    binaryCode = ''.join('{0:06b}'.format(table.index(char), 'b') for char in string.rstrip('\n').rstrip('='))
    answer = ''

    for i in range(0, len(binaryCode) - 7, 8):
        answer += chr(int(binaryCode[i: i + 8], 2))

    return answer


def errorInfo():
    print('Give arguments:\n'
          '--encode fileToEncode fileToWriteAnswer\nor\n'
          '--decode fileToDecode fileToWriteAnswer\n')


def main():
    if len(sys.argv) < 4:
        errorInfo()
        exit()

    with open(sys.argv[2], 'r') as dataFile:
        with open(sys.argv[3], 'w') as answerFile:
            if sys.argv[1] == '--encode':
                answerFile.write(encode(dataFile.read()))
            elif sys.argv[1] == '--decode':
                answerFile.write(decode(dataFile.read()))
            else:
                errorInfo()


if __name__ == '__main__':
    main()
