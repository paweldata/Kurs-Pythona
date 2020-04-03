from random import randint
from queue import Queue


class Tree:
    def __init__(self, h):
        self.__height = h
        self.__root = self.__getRandomTree(h)

    def showDFS(self):
        self.__showDFSRecursion(self.__root)
        print()

    def showBFS(self):
        queue = Queue()
        queue.put(self.__root)
        while not queue.empty():
            node = queue.get()
            print(node[0], end=' ')
            for i in range(1, len(node)):
                if node[i] is not None:
                    queue.put(node[i])
        print()

    def __getRandomTree(self, h):
        return [str(randint(1, 9))] + [self.__getRandomTree(h - 1) for _ in range(randint(1, 4))] if h > 1 \
            else [str(randint(1, 9)), None, None]

    def __showDFSRecursion(self, node):
        print(node[0], end=' ')
        for i in range(1, len(node)):
            if node[i] is not None:
                self.__showDFSRecursion(node[i])


def main():
    tree = Tree(4)
    print('DFS : ', end='')
    tree.showDFS()
    print('BFS : ', end='')
    tree.showBFS()


if __name__ == '__main__':
    main()
