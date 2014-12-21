import time
import math
import random

class Brain(object):

    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.inputs = [0.0] * input_size
        self.hidden = [0.0] * hidden_size
        self.output = [0.0] * output_size

        self.ih_weights = []
        self.ho_weights = []

        for i in xrange(self.input_size):
            temp = []
            for h in xrange(self.hidden_size):
                random.seed(time.time())
                temp.append(random.uniform(-1.0,1.0))
            self.ih_weights.append(temp)
            
        for h in xrange(self.hidden_size):
            temp = []
            for o in xrange(self.output_size):
                random.seed(time.time())
                temp.append(random.uniform(-1.0,1.0))
            self.ho_weights.append(temp)
    # end def __init__
    
    def sigmoid(self, x):
        return (1 / (1 + math.exp(-x)))
    # end def sigmoid
    
    def run_brain(self, location):
        self.inputs[0] = (self.inputs[0] - location[0])
        self.inputs[1] = (self.inputs[1] - location[1])
        
        for h in xrange(self.hidden_size):
            x = 0.0
            for i in xrange(self.input_size):
                self.ih_weights[i][h] -= (self.ih_weights[i][h] * 0.01)
                x += self.inputs[i] * self.ih_weights[i][h]
            self.hidden[h] = (1 / (1 + math.exp(-x)))
            
        for o in xrange(self.output_size):
            x = 0.0
            for h in xrange(self.hidden_size):
                self.ho_weights[h][o] -= (self.ho_weights[h][o] * 0.01)
                x += self.hidden[h] * self.ho_weights[h][o]
            self.output[o] = (1 / (1 + math.exp(-x)))
            
        if self.output[0] == max(self.output):
            return 0
        elif self.output[1] == max(self.output):
            return 1
        elif self.output[2] == max(self.output):
            return 2
        elif self.output[3] == max(self.output):
            return 3
        
        #return self.output
    # end def run_brain
    
    def strengthen_weights(self):
        for h in xrange(self.hidden_size):
            for i in xrange(self.input_size):
                self.ih_weights[i][h] += (self.ih_weights[i][h] * 0.01)
                
        for o in xrange(self.output_size):
            for h in xrange(self.hidden_size):
                self.ho_weights[h][o] += (self.ho_weights[h][o] * 0.01)
    # end def strengthen_weights
# end class Brain