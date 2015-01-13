# -*- coding: utf-8 -*-

# bug.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
# Created..........2015-01-10
# Last Modified....2015-01-10
#
# This module contains the bug class and was developed for use in the Bugs
# project.


# Import custom modules
import brain
import food

# Import modules from standard libraries
import time
import math
import random


class Bug(object):
  """The bug class is used to represent a single bug. Each bug will have a
  series of qualities that are randomly assigned unless provided. This class
  contains a series of functions so a bug may make descisions and perforrm a
  variety of actions.
  
  """
    
    def __init__(self, brain, health, hunger, size, color, gender, offspring, location):
        random.seed(time.time())
        
        self.brain    = brain
        self.health   = health
        self.hunger   = hunger
        self.
        self.location = [random.randint(min_grid_edge,max_grid_edge),random.randint(min_grid_edge,max_grid_edge)]
        self.count    = 0
        self.age      = 0
        self.goal     = [0,0]
    # end def __init__
    

    def time_tick(self,train):
        #if self.energy <= 0:
        #    return False
        self.energy -= 1
        
        if train:
            direction = self.brain.train_brain([(self.location[0]-self.goal[0]),(self.location[1]-self.goal[1])])
        else:
            direction = self.brain.run_brain([(self.location[0]-self.goal[0]),(self.location[1]-self.goal[1])])
        #direction = direction[:]
        direction = direction.index(max(direction))
        
        if direction == 0:
            self.location[0] += 1
        elif direction == 1:
            self.location[0] += 1
            self.location[0] += 1
        elif direction == 2:
            self.location[1] += 1
        elif direction == 3:
            self.location[0] -= 1
            self.location[1] += 1
        elif direction == 4:
            self.location[0] -= 1
        elif direction == 5:
            self.location[0] -= 1
            self.location[1] -= 1
        elif direction == 6:
            self.location[1] -= 1
        elif direction == 7:
            self.location[0] += 1
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
            self.energy = 50
            self.count += 1
            return True
        
        return False
    # end def time_tick


    def attack(self, other_bug):
        return True
    # end def attack
    
    
    def distance_to_goal(self):
        x_distance = ((self.goal[0] - self.location[0])**2)
        y_distance = ((self.goal[1] - self.location[1])**2)
        
        return math.sqrt(x_distance + y_distance)
    # end def distance_to_goal


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
                    
        return Bug(new_brain, 50, self.max_grid, self.min_grid)
    # end def procreate
    
# end class Bug