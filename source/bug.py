import time
import math
import random

class Bug(object):
    
    def __init__(self, brain, health, energy, size, legs, food, gender, babies, grid_size):
        """This function will initialize a bug with pre-defined values, a brain, and then
        generate a unique id. All of these bug qualities can be randomly generated or
        static amoung all bugs in the population. Bug ID will be stored in a class
        variable so that there is no duplication of live bug ID's.
        
        :param self: The current instance of this bug class. This will let the bug
                      define its instance variable.
        
        :param brain: The brain of this bug, currently only responsible for movement.
                       This will be a pointer to a brain object specific to the bug.
        
        :param health: The starting health of this bug.
        
        :param energy: The max energy of this bug. This input will also be used to
                        set the initial energy level of the bug.
        
        :param size: The size of this bug. The larger the bug the more damage when
                      attacking but means more energy expenditure.
        
        :param legs: The number of legs this bug has. The more legs the faster the
                      bug can move but means more energy expenditure.
        
        :param food: The food type this bug eats. This can be C, H, or O for each
                      of the different eating types.
        
        :param gender: The gender of this bug. This value can be M or F as we are
                        going with traditional gender roles.
        
        :param babies: The maximum number of offspring this bug is capable of
                        producing.
        
        """
        
        random.seed(time.time())
        
        self.health         = health
        self.brain          = brain
        self.current_energy = energy
        self.max_energy     = energy
        self.size           = size
        self.legs           = legs
        self.food           = food
        self.gender         = gender
        self.babies         = babies
        self.grid_size      = grid_size
        self.location       = [0,0]
        self.children       = 0
        self.count          = 0
        self.age            = 1
        self.goal           = [20,20]
    # end def __init__
    
    def set_goal(self, goal):
        self.brain.inputs[0] = goal[0]
        self.brain.inputs[1] = goal[1]
        self.goal = goal
    # end def set_goal
    
    def valid_move(self, move):
        result = 0
      
        if move == 0:
            result = self.location[0] + 1
        elif move == 1:
            result = self.location[0] - 1
        elif move == 2:
            result = self.location[1] + 1
        elif move == 3:
            result = self.location[1] - 1
            
        if result <= 39 and result >= 0:
            return True
            
        return False
    # end def valid_move
    
    def time_tick(self):
        self.current_energy -= 1
        direction = self.brain.run_brain(self.location)
        
        '''
        x1 = -999999
        x2 = 0
        for i in xrange(len(direction)):
            if direction[i] >= x1 and self.valid_move(i):
                x1 = direction[i]
                x2 = i
        '''
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
        
        if abs(self.location[0] - self.goal[0]) <= 1 and abs(self.location[1] - self.goal[1]) <= 1:
            self.current_energy = 100
            self.count += 1
            self.age += 1
            self.brain.strengthen_weights()
            return True
        
        return False
    # end def time_tick
    
    def generate_id(cls):
        random.seed(time.time())
        try:
            code = random.random()
            
            while code in cls.bugs:
                code = random.random()
            
            cls.bugs.append(code)
        except:
            code     = random.random()
            cls.bugs = [code]
            
        return code
    # end def generate_id
    
    def __str__(self):
        return 'Code: ' + str(self.bug_id) + '\nAge: ' + str(self.age) + '\nChildren: ' + str(self.children) + '\nHealth: ' + str(self.health) + '\nEnergy: ' + str(self.current_energy) + '\nSize: ' + str(self.size) + '\nLegs: ' + str(self.legs) + '\nFood: ' + str(self.food) + '\nGender: ' + str(self.gender) + '\nBabies: ' + str(self.babies) + '\nLocation: ' + str(self.location)
    # end def __str__
    
# end class Bug