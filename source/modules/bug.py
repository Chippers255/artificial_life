import brain
import time
import math
import random

class Bug(object):
    
    def __init__(self, brain, energy, max_grid_edge, min_grid_edge):
        random.seed(time.time())
        
        self.brain    = brain
        self.energy   = energy
        self.max_grid = max_grid_edge
        self.min_grid = min_grid_edge
        self.location = [random.randint(min_grid_edge,max_grid_edge),random.randint(min_grid_edge,max_grid_edge)]
        self.count    = 0
        self.age      = 0
        self.goal     = [random.randint(min_grid_edge,max_grid_edge),random.randint(min_grid_edge,max_grid_edge)]
    # end def __init__
    

    def time_tick(self,modify_weights):
        self.energy -= 1

        direction = self.brain.train_brain([(self.location[0]-self.goal[0]),(self.location[1]-self.goal[1])],modify_weights)
        direction = direction.index(max(direction))
        
        if direction == 0:
            self.location[0] += 1
        elif direction == 1:
            self.location[0] -= 1
        elif direction == 2:
            self.location[1] += 1
        elif direction == 3:
            self.location[1] -= 1
            
        if self.location[0] > self.max_grid:
            self.location[0] = self.min_grid
        elif self.location[0] < self.min_grid:
            self.location[0] = self.max_grid
        if self.location[1] > self.max_grid:
            self.location[1] = self.min_grid
        elif self.location[1] < self.min_grid:
            self.location[1] = self.max_grid
        
        if self.location[0] == self.goal[0] and self.location[1] == self.goal[1]:
            self.energy = 100
            self.count += 1
            return True
        
        return False
    # end def time_tick


    def procreate(self, other_bug, mutation_chance):
        random.seed()

        new_brain = brain.Brain(self.brain.input_size,self.brain.hidden_size,self.brain.output_size)
        for i in xrange(self.brain.input_size):
            for h in xrange(self.brain.hidden_size):
                if random.random() <= mutation_chance:
                    new_brain.ih_weights[i][h] = random.uniform(-1.0,1.0)
                else:
                    new_brain.ih_weights[i][h] = random.choice([self.brain.ih_weights[i][h],other_bug.brain.ih_weights[i][h]])
            
        for h in xrange(self.brain.hidden_size):
            for o in xrange(self.brain.output_size):
                if random.random() <= mutation_chance:
                    new_brain.ho_weights[h][o] = random.uniform(-1.0,1.0)
                else:
                    new_brain.ho_weights[h][o] = random.choice([self.brain.ho_weights[h][o],other_bug.brain.ho_weights[h][o]])
                    
        new_bug = Bug(new_brain, 100, self.max_grid, self.min_grid)
        
        return new_bug
    # end def procreate
    
# end class Bug