import matplotlib.pyplot as plt
import numpy as np
from random import randint
import matplotlib.animation as animation


fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [], lw=2)


def init():
    ax.set_xlim(0, 2)
    ax.set_ylim(-1, 1)
    return line,


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


def relu(x):
    return x * (x > 0)


def relu_derivative(x):
    return 1. * (x > 0)


def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):
    return 1.0 - np.tanh(x)**2


class NeuralNetwork:
    def __init__(self, x, y, f1, f1_derivative, f2, f2_derivative, f3, f3_derivative):
        self.input = x
        self.weights1 = np.random.rand(10, 1)
        self.weights2 = np.random.rand(10, 10)
        self.weights3 = np.random.rand(1, 10)
        self.y = y
        self.output = np.zeros(self.y.shape)

        self.eta = 0.01
        self.function1 = f1
        self.function1_derivative = f1_derivative
        self.function2 = f2
        self.function2_derivative = f2_derivative
        self.function3 = f3
        self.function3_derivative = f3_derivative

        self.counter = 0

    def showAnimation(self):
        anim = animation.FuncAnimation(fig, self.__animate, init_func=init, interval=50)
        plt.show()

    def __feedforward(self, i):
        self.layer1 = self.function1(np.dot(self.input[i], self.weights1.T))
        self.layer2 = self.function2(np.dot(self.layer1, self.weights2.T))
        self.output[i] = self.function3(np.dot(self.layer2, self.weights3.T))

    def __backprop(self, i):
        delta3 = (self.y[i] - self.output[i]) * self.function3_derivative(self.output[i])
        d_weights3 = self.eta * np.dot(delta3.T, self.layer2)
        delta2 = self.function1_derivative(self.layer2) * np.dot(delta3, self.weights3)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.function1_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input[i])

        self.weights1 += d_weights1
        self.weights2 += d_weights2
        self.weights3 += d_weights3

    def __getMSE(self):
        result = 0
        for i in range(len(self.input)):
            result += (self.input[i] - self.output[i]) ** 2
        return round(result / len(self.input), 5)

    def __animate(self, j):
        self.counter += 1000
        plt.title('Try ' + str(self.counter) + '   MSE ' + str(self.__getMSE()))
        for i in range(1000):
            self.__feedforward(i % len(self.input))
            self.__backprop(i % len(self.input))
        line.set_data(self.input, self.output)
        return line,


def main():
    x = np.linspace(0, 2, 161)
    y = np.sin((3 * np.pi / 2) * x)

    nn = NeuralNetwork(x, y, tanh, tanh_derivative, tanh, tanh_derivative, tanh, tanh_derivative)
    nn.showAnimation()


if __name__ == '__main__':
    main()
