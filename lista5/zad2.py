import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def getData(filename):
    data = pd.read_csv(filename)
    array = data[['userId', 'movieId', 'rating']].to_numpy()

    films = pd.read_csv('movies.csv')
    films = films[['movieId', 'title']].to_numpy()
    films = np.array([row for row in films if int(row[0]) < 10000])

    array = np.array([row for row in array if row[1] < 10000])
    maxUserId = int(np.max(array[:, 0]))

    x = np.array([np.zeros(int(films[-1][0]) + 1) for _ in range(maxUserId)])
    for row in array:
        x[int(row[0]) - 1][int(row[1])] = row[2]

    return x, films


def main():
    array, films = getData('ratings.csv')

    my_ratings = np.zeros((9019, 1))
    my_ratings[2571] = 5  # 2571 - Matrix
    my_ratings[32] = 4  # 32 - Twelve Monkeys
    my_ratings[260] = 5  # 260 - Star Wars IV
    my_ratings[1097] = 4

    array_norm = np.nan_to_num(array / np.linalg.norm(array, axis=0))
    my_ratings_norm = np.nan_to_num(np.array(my_ratings) / np.linalg.norm(my_ratings))
    z = np.dot(array_norm, my_ratings_norm)
    z_norm = z / np.linalg.norm(z)

    result = np.dot(array_norm.T, z_norm)
    answer = np.array([[row[0], i] for i, row in enumerate(result) if i in films[:, 0]])
    answer = np.array([[row[0], films[i][1]] for i, row in enumerate(answer)])
    answer = answer[answer[:, 0].argsort()][::-1]

    print('First 20 films:')
    print(answer[:20])


if __name__ == '__main__':
    main()
