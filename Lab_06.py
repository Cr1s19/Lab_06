import random
import math

#----- TRAINING -----#

def rand(a, b):
    return (b - a) * random.random() + a

def sigmoid(x):
    #return 1.0 / (1.0 + math.exp(-x))
    return math.tanh(x)

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
        actual_result = self.activation_function (total_sum)
        #print("ac ", actual_result, "es ", expected_result)
        error = expected_result - actual_result
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + self.learning_rate * error * inputs[i]
        return error


def main():
    #Read data set
    training_inputs = []
    training_outputs = []
    testing_inputs = [0.0] * 4

    print("Perceptron")
    with open("perceptron_dataSet2.txt", "r") as infile:
        for line in infile:
            ins = [float(x) for x in line.split(',')]
            training_outputs.append(ins.pop())
            training_inputs.append(ins)
    print(training_inputs)
    print(training_outputs)

    num = len(training_inputs)
    print(num)

    learning_rate = 1
    max_iterations = 10000
    classify = Perceptron(4, learning_rate)

    i = 0
    while i < max_iterations:
        error = classify.training(training_inputs[i%num], training_outputs[i%num])
        i = i + 1
        print(error, i)

    #for i in range(len(training_inputs)):
        #ans = classify.feed_forward(training_inputs[i])
        #ans2 = classify.activation_function(ans)
        #print(ans2)

    option = 'a'
    while(option == 'a' or option == 'b'):
        print("BANKNOTE AUTHENTICATION")
        print("a. Select testing data from training data set")
        print("b. Insert new data")
        print("c. Exit")
        option = input("Option? (a/b): ")

        if(option == 'a'):
            index = int(input("   Select the number (0 - %d): " % (num-1)))
            if(index >= 0 and index < num):
                print("     Variance of Wavelet Transfoerd image: %f" % (training_inputs[index][0]))
                print("     Skewness of Wavelet Transformed image: %f" % (training_inputs[index][1]))
                print("     Curtosis of Wavelet Transformed image: %f" % (training_inputs[index][2]))
                print("     Entropy of image: %f" % (training_inputs[index][3]))
                print()
                aux_sum = classify.feed_forward(training_inputs[index])
                output = classify.activation_function(aux_sum)
                print("     Class: ", output)

        elif(option == 'b'):
            testing_inputs[0] = float(input("Variance of Wavelet Transfoerd image: "))
            testing_inputs[1] = float(input("Skewness of Wavelet Transformed image: "))
            testing_inputs[2] = float(input("Curtosis of Wavelet Transformed image: "))
            testing_inputs[3] = float(input("Entropy of image: "))
            print()
            aux_sum = classify.feed_forward(testing_inputs)
            output = classify.activation_function(aux_sum)
            print("     Class: ", output)
        print()


if __name__ == "__main__":
    main()

#----- TESTING -----#
#read user input
