import random

#----- TRAINING -----#


class Perceptron:
    def __init__(self, rate):
        self.weights = []
        self.learning_rate = rate

    def random_weigths(self, n):
        #random n weights from 1 to 9
        self.weights = random.sample(range(1, 100), n)

    def activation_function(self, value):
        #threshold
        if value > 0:
            return 1
        else:
            return -1

    def feed_forward(self, inputs):
        total_sum = 0
        #Multiply each input by its weight, sum all
        for i in range(len(inputs)):
            total_sum += inputs[i] * self.weights[i]
        return total_sum

    def training(self, inputs, expected_result):
        total_sum = self.feed_forward(inputs)
        actual_result = self.activation_function(total_sum)
        error = expected_result - actual_result
        for i in range(len(self.weights)):
            self.weights += self.learning_rate * error * inputs[i]
        return error

#while(1):
#    a = Perceptron()
#    a.random_weigths(5)
#    print(a.weights)


def main():
    #Read data set
    training_inputs = []
    training_outputs = []
    test_inputs = []

    classify = Perceptron(0.5)
    error = 10
    max_iterations = 2000
    tolerance = 0.1
    i = 0
    while error > tolerance and i < max_iterations:
        error = classify.training(training_inputs[i], training_outputs[i])
        i += 1

    test_inputs[0] = input("Age of patient at time of operation: ")
    test_inputs[1] = input("Patient's year of operation: ")
    test_inputs[2] = input("Number of positive axillary nodes detected: ")
    aux_sum = classify.feed_forward(test_inputs)
    output = classify.activation_function(aux_sum)
    return output


if __name__ == "__main__":
    main()

#----- TESTING -----#
#read user input
