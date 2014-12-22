import math
import random

class Brain(object):

    def __init__(self, input_size, hidden_size, output_size):
        random.seed()

        self.input_size  = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.inputs = [0.0] * input_size
        self.hidden = [0.0] * hidden_size
        self.output = [0.0] * output_size

        self.ih_weights = []
        self.ho_weights = []

        for i in xrange(self.input_size):
            self.ih_weights.append([random.uniform(-1.0, 1.0) for x in xrange(self.hidden_size)])
            
        for h in xrange(self.hidden_size):
            self.ho_weights.append([random.uniform(-1.0, 1.0) for x in xrange(self.output_size)])
    # end def __init__
    

    def sigmoid(self, x):
        return (1 / (1 + math.exp(-x)))
    # end def sigmoid


    def tanh(self, x):
        return math.tanh(x)
    # end def tanh


    def weaken_weights(self):
        for h in xrange(self.hidden_size):
            for i in xrange(self.input_size):
                self.ih_weights[i][h] -= (self.ih_weights[i][h] * 0.01)
                
        for o in xrange(self.output_size):
            for h in xrange(self.hidden_size):
                self.ho_weights[h][o] -= (self.ho_weights[h][o] * 0.01)
    # end def strengthen_weights
    

    def strengthen_weights(self):
        for h in xrange(self.hidden_size):
            for i in xrange(self.input_size):
                self.ih_weights[i][h] += (self.ih_weights[i][h] * 0.01)
                
        for o in xrange(self.output_size):
            for h in xrange(self.hidden_size):
                self.ho_weights[h][o] += (self.ho_weights[h][o] * 0.01)
    # end def strengthen_weights

    
    def run_brain(self, inputs, tweak_bool):
        self.inputs = inputs
        
        if random.random() <= 0.01 and tweak_bool:
            random.choice([self.weaken_weights(),self.strengthen_weights()])
        
        for h in xrange(self.hidden_size):
            x = 0.0
            for i in xrange(self.input_size):
                x += self.inputs[i] * self.ih_weights[i][h]
            self.hidden[h] = self.sigmoid(x)
            
        for o in xrange(self.output_size):
            x = 0.0
            for h in xrange(self.hidden_size):
                x += self.hidden[h] * self.ho_weights[h][o]
            self.output[o] = self.sigmoid(x)

        return self.output.index(max(self.output))
    # end def run_brain

# end class Brain