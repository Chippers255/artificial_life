import sys
import time
import math
import random

from modules import *

def display_grid(population, goal, grid_size):
    grid = [['.' for col in xrange(grid_size)] for row in xrange(grid_size)]
    
    for i in population:
        grid[i.location[0]][i.location[1]] = 'B'
      
    for f in goal:
      grid[f[0]][f[1]] = 'F'
    
    for row in grid:
        line = ''
        for column in row:
            line += column + ' '
        print line
# end def display_grid

def generate_population(size):
    population = []
    for x in xrange(size):
        b = brain.Brain(2,8,4)
        i = bug.Bug(b, 50, 39,0)
        population.append(i)
        
    return population
# end def generate_population

def train_population(population, length, size, generation):
    count = 0
    random.seed()
    food = [random.randint(0,39),random.randint(0,39)]
    for t in xrange(length):
        for i in population:
            i.goal = food
            if i.time_tick(True):
                count += 1
                food = [random.randint(0,39),random.randint(0,39)]
    
    new_population = []
    
    while len(new_population) < size:
        new_population.append(selection.tournament_distance_selection(population,len(population)/6))
        
    if size > 20:
        new_population.extend(generate_population(1))
    
    return new_population, count
# end def train_population

def tune_population(population, length, size, generation):
    count = 0
    random.seed()
    food = [random.randint(0,39),random.randint(0,39)]
    for t in xrange(length):
        for i in population:
            i.goal = food
            if i.time_tick(True):
                count += 1
                food = [random.randint(0,39),random.randint(0,39)]
    
    new_population = []
    
    while len(new_population) < size:
        new_population.append(selection.tournament_count_selection(population,len(population)/4))
    
    return new_population, count
# end def train_population

def stop_check(population):
    check = population[0]
    for i in population:
        if i.brain.ih_weights != check.brain.ih_weights or i.brain.ho_weights != check.brain.ho_weights:
            return False
    return True
# end def stop_check

def run_population(population, length):
    count = 0
    random.seed()
    food = []
    for i in xrange(1):
        food.append([random.randint(0,39),random.randint(0,39)])
    for t in xrange(length):
        for i in population:
            best = 500
            bb = None
            for f in food:
                distance = ((f[0] - i.location[0])**2) + ((f[1] - i.location[1])**2)
                distance = math.sqrt(distance)
                if distance < best:
                    best = distance
                    bb = f
            i.goal = bb
            if i.time_tick(False):
                count += 1
                food.remove(bb)
                food.append([random.randint(0,39),random.randint(0,39)])
        sys.stderr.write("\x1b[2J\x1b[H")
        print 'Population: ' + str(len(population))
        print 'Food Count: ' + str(count)
        print
        display_grid(population,food,40)
        time.sleep(0.05)
# end def run_population

population = generate_population(100)
pop_size   = 100

t1 = time.time()

for i in xrange(2000):
    print i
    if i%100 == 0 and pop_size > 20:
        pop_size -= 10
    population, count = train_population(population, 50, pop_size, i)
    if count >= pop_size/3:
        break

print (time.time() - t1)
time.sleep(5)

file = open('saved_weights.csv','w')

for i in population:
    line = ''
    for inputs in xrange(2):
        for hidden in xrange(6):
            line += str(i.brain.ih_weights[inputs][hidden]) + ','
    
    for hidden in xrange(6):
        for output in xrange(4):
            line += str(i.brain.ho_weights[hidden][output]) + ','
            
    line += '\n'
    file.write(line)
    file.flush()

file.close()

for i in xrange(100):
    run_population(population, 200)