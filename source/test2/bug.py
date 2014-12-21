import time
import math
import random

class Bug(object):
    
    def __init__(self, health, energy, size, legs, food, gender, babies, location):
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
                          
        :param location: The starting location for this bug.
        
        """
        
        self.health         = health
        #self.brain          = brain
        self.current_energy = energy
        self.max_energy     = energy
        self.size           = size
        self.legs           = legs
        self.food           = food
        self.gender         = gender
        self.babies         = babies
        self.location       = location
        self.set_random_position(39)
        self.children       = 0
        self.age            = 0
        #self.bug_id         = self.generate_id()
    # end def __init__
    
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
        
    def set_brain(self, food):
        self.i_size = 2
        self.h_size = 6
        self.o_size = 4
        
        self.inputs = [self.location[0] - food[0], self.location[1] - food[1]]
        self.hidden = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.output = [0.0, 0.0, 0.0, 0.0]
        
        self.ih_weights = []
        self.ho_weights = []
        
        for i in xrange(self.i_size):
            temp = []
            for h in xrange(self.h_size):
                random.seed(time.time())
                temp.append(random.uniform(-1.0,1.0))
            self.ih_weights.append(temp)
            
        for h in xrange(self.h_size):
            temp = []
            for o in xrange(self.o_size):
                random.seed(time.time())
                temp.append(random.uniform(-1.0,1.0))
            self.ho_weights.append(temp)
    # end def set_brain
    
    def set_food(self, food):
        self.inputs[0] = food[0]
        self.inputs[1] = food[1]
        
    def set_random_position(self, size):
        random.seed()
        self.location[0] = random.randint(0,size)
        self.location[1] = random.randint(0,size)
    
    def run_brain(self):
        if self.inputs[0] == self.location[0] and self.inputs[1] == self.location[1]:
            return True
        
        # hidden activations
        for h in xrange(self.h_size):
            sum = 0.0
            for i in xrange(self.i_size):
                sum += self.inputs[i] * self.ih_weights[i][h]
            self.hidden[h] = (1 / (1 + math.exp(-sum)))
            
        for o in xrange(self.o_size):
            sum = 0.0
            for h in xrange(self.h_size):
                sum += self.hidden[h] * self.ho_weights[h][o]
            self.output[o] = (1 / (1 + math.exp(-sum)))
            
        '''if self.output[0] <= 0.33:
            self.location[0] -= 1
        elif self.output[0] > 0.33 and self.output[0] < 0.66:
            self.location[0] += 0
        else:
            self.location[0] += 1
            
        if self.output[1] <= 0.33:
            self.location[1] -= 1
        elif self.output[1] > 0.33 and self.output[1] < 0.66:
            self.location[1] += 0
        else:
            self.location[1] += 1'''
            
        #print self.output
        #print max(self.output)
        
        if self.output[0] == max(self.output):
            self.location[0] += 1
        #elif self.output[0] == max(self.output):
        #    self.location[0] += 1
        #    self.location[1] += 1
        #elif self.output[2] == max(self.output):
        #    self.location[0] += 1
        #    self.location[1] -= 1
        elif self.output[1] == max(self.output):
            self.location[0] -= 1
        #elif self.output[4] == max(self.output):
        #    self.location[0] -= 1
        #    self.location[1] += 1
        #elif self.output[5] == max(self.output):
        #    self.location[0] -= 1
        #    self.location[1] -= 1
        elif self.output[2] == max(self.output):
            self.location[1] += 1
        elif self.output[3] == max(self.output):
            self.location[1] -= 1
        
        if self.location[0] > 39 or self.location[0] < 0:
            self.location[0] = abs(abs(self.location[0]) - 39)
            
        if self.location[1] > 39 or self.location[1] < 0:
            self.location[1] = abs(abs(self.location[1]) - 39)
    # end def run_brain
    
    def time_tick(self):
        return 0
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