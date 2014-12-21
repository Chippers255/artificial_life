import brain
import time
import math
import random

class Bug(object):
    
    def __init__(self, brain, energy):
        random.seed(time.time())
        
        self.brain    = brain
        self.energy   = energy
        self.location = [random.randint(0,39),random.randint(0,39)]
        self.count    = 0
        self.age      = 1
        self.goal     = [20,20]
    # end def __init__
    
    def time_tick(self):
        self.energy -= 1
        direction = self.brain.run_brain([(self.location[0]-self.goal[0]),(self.location[1]-self.goal[1])])
        
        if direction == 0:
            self.location[0] += 1
        elif direction == 1:
            self.location[0] -= 1
        elif direction == 2:
            self.location[1] += 1
        elif direction == 3:
            self.location[1] -= 1
            
        if self.location[0] > 39 or self.location[0] < 0:
            self.location[0] = abs(abs(self.location[0]) - 39)
        if self.location[1] > 39 or self.location[1] < 0:
            self.location[1] = abs(abs(self.location[1]) - 39)
        
        if self.location[0] == self.goal[0] and self.location[1] == self.goal[1]:
            self.energy = 100
            self.count += 1
            return True
        
        return False
    # end def time_tick
    
# end class Bug