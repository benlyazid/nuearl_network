import numpy
import scipy.special
class nueralNetwork:

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learningrate):
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes
        self.lr = learningrate
        self.w_i_h = numpy.random.rand(self.inodes, self.hnodes)
        self.w_h_o = numpy.random.rand(self.hnodes, self.onodes)
        self.activation_function = lambda x: scipy.special.expit(x)

    def train(self):
        pass

    def query(self, input_list):
        inputs = numpy.array(input_list, ndmin=2).T
        print(inputs)
        hidden_inputs = numpy.dot(self.w_i_h, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.w_h_o, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        print(final_outputs)
        return final_outputs

nueral = nueralNetwork(3, 3, 3, 0.001)
nueral.query([1.2, 0.5, -1.5])
