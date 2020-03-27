def flatten(tab):
    for elem in tab:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem


def main():
    print(list(flatt([[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]])))


if __name__ == '__main__':
    main()
