import sys
import time
import math
import random

from modules import *

from psychopy import visual, core, data, event, logging, sound, gui, misc, monitors
from psychopy.constants import *
import numpy as np
import os
import Image
import ctypes

MONITOR_NAME = 'tomimac'

def display_grid(population, goal, grid_size):
    grid = [['.' for col in xrange(grid_size)] for row in xrange(grid_size)]
    
    for i in population:
        grid[i.location[0]][i.location[1]] = 'B'
        
    grid[goal[0]][goal[1]] = 'F'
    
    for row in grid:
        line = ''
        for column in row:
            line += column + ' '
        print line
# end def display_grid

def generate_population(size):
    population = []
    for x in xrange(size):
        b = brain.Brain(2,6,4)
        i = bug.Bug(b, 100, 20, -20)
        population.append(i)
        
    return population
# end def generate_population

def train_population(population, length, size, generation):
    count = 0
    random.seed()
    food = [random.randint(-20,20),random.randint(-20,20)]
    for t in xrange(length):
        for i in population:
            i.goal = food
            if i.time_tick():
                count += 1
                food = [random.randint(-20,20),random.randint(-20,20)]
        #time.sleep(0.05)
    
    new_population = []
    
    while len(new_population) < size:
        i1 = tournament_selection(population)
        i2 = tournament_selection(population)
        new_population.append(i1.procreate(i2,0.01))
        
    if size > 20:
        new_population.extend(generate_population(1))
    
    return new_population
# end def train_population

def tournament_selection(population):
    random.seed()
    
    tournament_size = int(len(population) / 6)
    best = population[random.randint(0,len(population)-1)]
    
    for i in xrange(tournament_size):
        individual = population[random.randint(0,len(population)-1)]
        distance1 = ((individual.goal[0] - individual.location[0])**2) + ((individual.goal[1] - individual.location[1])**2)
        distance2 = ((best.goal[0] - best.location[0])**2) + ((best.goal[1] - best.location[1])**2)
        distance1 = math.sqrt(distance1) - individual.count
        distance2 = math.sqrt(distance2) - best.count
        if distance1 < distance2:
            best = individual
        
    return best
# def end tournament_selection

def mate_population(i1, i2):
    random.seed()
    b = brain.Brain(2,6,4)
    for i in xrange(2):
        for h in xrange(6):
            if random.random() <= 0.01:
                b.ih_weights[i][h] = random.uniform(-1.0,1.0)
            else:
                b.ih_weights[i][h] = random.choice([i1.brain.ih_weights[i][h],i2.brain.ih_weights[i][h]])
            
    for h in xrange(6):
        for o in xrange(4):
            if random.random() <= 0.01:
                b.ho_weights[h][o] = random.uniform(-1.0,1.0)
            else:
                b.ho_weights[h][o] = random.choice([i1.brain.ho_weights[h][o],i2.brain.ho_weights[h][o]])
                
    new_bug = bug.Bug(b, 100)
    
    return new_bug
# end def mate_population

def run_population(population, length, pop_list, win):
    food_rect = visual.Rect(win, width=0.5, height=0.5, fillColor=[1,-1,-1], fillColorSpace='rgb', lineColor=[1,-1,-1], lineColorSpace='rgb')
    count = 0
    random.seed()
    food = [random.randint(-20,20),random.randint(-20,20)]
    food_rect.setPos(food)
    food_rect.setAutoDraw(True)
    for t in xrange(length):
        for i in population:
            i.goal = food
            if i.time_tick():
                count += 1
                food = [random.randint(-20,20),random.randint(-20,20)]
                food_rect.setPos(food)
                food_rect.setAutoDraw(True)
        for i in xrange(len(population)):
            pop_list[i].setPos(population[i].location)
            pop_list[i].setAutoDraw(True)
        win.flip()
        time.sleep(0.03)
        if event.getKeys(["q"]):
            exit()
    food_rect.setAutoDraw(False)
    win.flip()
# end def run_population

population = generate_population(100)

pop_size = 100

for i in xrange(1100):
    if i%100 == 0 and pop_size > 20:
        pop_size -= 10
    population = train_population(population, 50, pop_size, i)
    print "Generation: " + str(i)

# Setup the Psychopy variables (screen, stimuli, sounds, ect)
win        = visual.Window(fullscr=True, screen=0, allowGUI=False, allowStencil=False, monitor=MONITOR_NAME, color=[0,0,0], colorSpace='rgb', units='deg')
mon        = monitors.Monitor(MONITOR_NAME)
trialClock = core.Clock()
eventClock = core.Clock()
keyResp    = event.BuilderKeyResponse()  # create an object of type KeyResponse
mouse      = event.Mouse(win=win)
    
file = open('saved_weights.csv','w')
pop_list = []

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
    pop_list.append(visual.Rect(win, width=0.5, height=0.5, fillColor=[-1,-1,-1], fillColorSpace='rgb', lineColor=[-1,-1,-1], lineColorSpace='rgb'))

file.close()

for i in xrange(20):
    run_population(population, 100, pop_list, win)