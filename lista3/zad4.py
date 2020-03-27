def quickSort1(tab):
    if len(tab) > 1:
        return quickSort1(list(filter(lambda x: x < tab[0], tab))) + \
               [tab[0]] + quickSort1(list(filter(lambda x: x > tab[0], tab)))
    return tab


def quickSort2(tab):
    if len(tab) > 1:
        return quickSort2([x for x in tab if x < tab[0]]) + \
               [tab[0]] + quickSort2([x for x in tab if x > tab[0]])
    return tab


def main():
    print(quickSort1([7, 4, 1, 8, 5, 2, 0, 9, 6, 3]))
    print(quickSort2([7, 4, 1, 8, 5, 2, 0, 9, 6, 3]))


if __name__ == '__main__':
    main()
