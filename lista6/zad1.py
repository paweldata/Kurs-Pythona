import numpy as np


def sigmoid(x):
    return 1.0/(1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


def relu(x):
    return x * (x > 0)


def relu_derivative(x):
    return 1. * (x > 0)


class NeuralNetwork:
    def __init__(self, x, y, f1, f1_derivative, f2, f2_derivative, eta):
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta
        self.function1 = f1
        self.function1_derivative = f1_derivative
        self.function2 = f2
        self.function2_derivative = f2_derivative

    def feedforward(self):
        self.layer1 = self.function1(np.dot(self.input, self.weights1.T))
        self.output = self.function2(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * self.function2_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.function1_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2


def calculate(nn):
    for _ in range(5000):
        nn.feedforward()
        nn.backprop()


def f(X, Y):
    nn1 = NeuralNetwork(X, Y, sigmoid, sigmoid_derivative, sigmoid, sigmoid_derivative, 0.5)
    calculate(nn1)
    print('1. sigmoid, 2. sigmoid, eta = 0.5')
    print(nn1.output.tolist())

    nn2 = NeuralNetwork(X, Y, sigmoid, sigmoid_derivative, relu, relu_derivative, 0.1)
    calculate(nn2)
    print('1. sigmoid, 2. relu, eta = 0.1')
    print(nn2.output.tolist())

    nn3 = NeuralNetwork(X, Y, relu, relu_derivative, sigmoid, sigmoid_derivative, 0.01)
    calculate(nn3)
    print('1. relu, 2. sigmoid, eta = 0.01')
    print(nn3.output.tolist())

    nn4 = NeuralNetwork(X, Y, relu, relu_derivative, relu, relu_derivative, 0.01)
    calculate(nn4)
    print('1. relu, 2. relu, eta = 0.01')
    print(nn4.output.tolist())

def main():
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])

    xorArray = np.array([[0], [1], [1], [0]])
    andArray = np.array([[0], [0], [0], [1]])
    orArray = np.array([[0], [1], [1], [1]])

    np.random.seed(17)

    print('XOR')
    f(X, xorArray)
    print()

    print('AND')
    f(X, andArray)
    print()

    print('OR')
    f(X, orArray)
    print()


if __name__ == '__main__':
    main()
