import numpy
import random

class nueralNetwork:

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learningrate):
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes
        self.lr = learningrate
    
    def train(self):
        return
    def query(self):
        print(10)

nueral = nueralNetwork(2, 3, 2, 0.001)
nueral.query()