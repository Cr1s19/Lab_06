import random
#----- TRAINING -----#


class Perceptron:
    def __init__(self, rate):
        self.weights = []
        self.learning_rate = rate

    def random_weigths(self, n):
        #random n weights from 1 to 9
        self.weights = random.sample(range(1, 10), n)

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


#read training data set
    #input
    #output

while(1):
    a = Perceptron()
    a.random_weigths(5)
    print(a.weights)


#----- TESTING -----#
#read user input
