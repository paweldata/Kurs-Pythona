def transposition(matrix):
    return [' '.join(string.split(' ')[j] for string in matrix) for j in range(len(matrix[0].split(' ')))]


def main():
    print(transposition(["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]))


if __name__ == '__main__':
    main()
