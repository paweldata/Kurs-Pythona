def allSubsets1(data):
    return list(map(lambda i: list(filter(lambda elem: i & (1 << data.index(elem)) == 0, data)), range(1 << len(data))))


def allSubsets2(data):
    return [[data[j] for j in range(len(data)) if i & (1 << j) == 0] for i in range(1 << len(data))]


def main():
    print(allSubsets1([1, 2, 3]))
    print(allSubsets2([1, 2, 3]))


if __name__ == '__main__':
    main()
