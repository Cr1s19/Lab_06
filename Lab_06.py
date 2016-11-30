import random
import math

#----- TRAINING -----#

def rand(a, b):
    return (b - a) * random.random() + a

class Perceptron:
    def __init__(self, num_input, rate):
        self.weights = [0.0] * num_input
        self.learning_rate = rate
        self.random_weigths(num_input)

    def random_weigths(self, num_input):
        #random n weights from 1 to 9
        for i in range(num_input):
            self.weights[i] = rand(-0.001, 0.001)
            print(self.weights[i])

    def activation_function(self, value):
        #threshold
        if value > 0:
            return 1
        else:
            return 0

    def feed_forward(self, inputs):
        total_sum = 0.0
        #Multiply each input by its weight, sum all
        for i in range(len(inputs)):
            total_sum = total_sum + inputs[i] * self.weights[i]
            #print("Total sum ", total_sum)
        return total_sum

    def training(self, inputs, expected_result):
        total_sum = self.feed_forward(inputs)
        actual_result = self.activation_function(total_sum)
        #print("ac ", actual_result, "es ", expected_result)
        error = expected_result - actual_result
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + self.learning_rate * error * inputs[i]
        return error


def main():
    #Read data set
    training_inputs = []
    training_outputs = []

    with open("data.in", "r") as infile:
        for line in infile:
            ins = [float(x) for x in line.split(',')]
            training_outputs.append(ins.pop())
            training_inputs.append(ins)
    print(training_inputs)
    print(training_outputs)

    num = len(training_inputs)
    print(num)

    classify = Perceptron(4, 0.5)
    max_iterations = 10000
    i = 0
    while i < max_iterations:
        error = classify.training(training_inputs[i%num], training_outputs[i%num])
        i = i+1
        print(error, i)


if __name__ == "__main__":
    main()
