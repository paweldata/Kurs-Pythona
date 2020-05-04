import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def getData(filename):
    data = pd.read_csv(filename)
    array = data[['userId', 'movieId', 'rating']].to_numpy()
    userId = sorted([row[0] for row in array if row[1] == 1])
    array = np.array([[userId.index(row[0]), row[1], row[2]] for row in array if row[0] in userId])
    maxFilmId = int(np.max(array))

    x = np.array([np.zeros(maxFilmId - 1) for _ in range(215)])
    y = np.zeros(215)
    for row in array:
        if row[1] > 1:
            x[int(row[0])][int(row[1]) - 2] = row[2]
        else:
            y[int(row[0])] = row[2]

    return x, y


def zad1(x, y, m):
    usersId = [i for i in range(215)]
    plt.xlabel('user')
    plt.ylabel('rate')

    if m < len(x[0]):
        x = x[:, :m]
        answer = np.linalg.lstsq(x, y, rcond=None)[0]
        plt.scatter(usersId, [sum(answer[i] * x[j][i] for i in range(m)) for j in range(len(x))])
        plt.title('m = ' + str(m))
    else:
        plt.scatter(usersId, y)
        plt.title('original')


def zad2(x, y, m):
    usersId = [i for i in range(200, 215)]
    plt.xlabel('user')
    plt.ylabel('rate')

    if m < len(x[0]):
        answer = np.linalg.lstsq(x[:200, :m], y[:200], rcond=None)[0]
        plt.scatter(usersId, [sum(answer[i] * x[j][i] for i in range(m)) for j in range(200, 215)])
        plt.title('m = ' + str(m))
    else:
        plt.scatter(usersId, y[200:])
        plt.title('original')


def main():
    x, y = getData('ratings.csv')

    # zad1
    plt.subplot(221)
    zad1(x, y, 10)
    plt.subplot(222)
    zad1(x, y, 1000)
    plt.subplot(223)
    zad1(x, y, 10000)
    plt.subplot(224)
    zad1(x, y, len(x[0]))
    plt.show()
    plt.close()

    # zad2
    plt.subplot(331)
    zad2(x, y, 10)
    plt.subplot(332)
    zad2(x, y, 100)
    plt.subplot(333)
    zad2(x, y, 200)
    plt.subplot(334)
    zad2(x, y, 500)
    plt.subplot(335)
    zad2(x, y, 1000)
    plt.subplot(336)
    zad2(x, y, 10000)
    plt.subplot(338)
    zad2(x, y, len(x[0]))
    plt.show()


if __name__ == '__main__':
    main()
