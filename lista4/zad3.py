from random import randint
from queue import Queue


class Node(object):
    def __init__(self, value):
        self.__value = value
        self.__children = []

    def addChild(self, child):
        self.__children.append(child)

    def getValue(self):
        return self.__value

    def getChildren(self):
        return self.__children


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
            print(node.getValue(), end=' ')
            for child in node.getChildren():
                queue.put(child)
        print()

    def __getRandomTree(self, h):
        node = Node(randint(1, 10))
        if h > 1:
            for _ in range(randint(1, 4)):
                node.addChild(self.__getRandomTree(h - 1))
        return node

    def __showDFSRecursion(self, node):
        print(node.getValue(), end=' ')
        for child in node.getChildren():
            self.__showDFSRecursion(child)


def main():
    tree = Tree(3)
    print('DFS : ', end='')
    tree.showDFS()
    print('BFS : ', end='')
    tree.showBFS()


if __name__ == "__main__":
    main()
