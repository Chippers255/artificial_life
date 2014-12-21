import bug
import sys
import time
import brain
import random

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
        b = brain.Brain(3,7,4)
        b.inputs[2] = 1
        b.hidden[6] = 1
        i = bug.Bug(b, 100, 100, random.randint(1,10), random.randint(2,10), random.choice(['H']), random.choice(['M','F']), random.randint(1,5), 40)
        i.set_goal([20,20])
        population.append(i)
        
    return population
# end def generate_population

def run_population(population, length, size, generation):
    count = 0
    random.seed()
    food = [random.randint(0,39),random.randint(0,39)]
    for t in xrange(length):
        for i in population:
            i.set_goal(food)
            if i.time_tick():
                count += 1
                food = [random.randint(0,39),random.randint(0,39)]
        sys.stderr.write("\x1b[2J\x1b[H")
        print len(population)
        print generation
        print count
        print
        display_grid(population,food,40)
        #time.sleep(0.05)
    
    population = [i for i in population if (i.current_energy > 0)]
    
    population.extend(generate_population(1))
    
    while len(population) < size:
        random.seed()
        i1 = tournament_selection(population)
        i2 = tournament_selection(population)
        population.append(mate_population(i1,i2))
        
    return population
# end def run_population

def tournament_selection(population):
    random.seed()
    tournament_size = int(len(population) / 4)
    best = population[random.randint(0,len(population)-1)]
    for i in xrange(tournament_size):
        individual = population[random.randint(0,len(population)-1)]
        if (best == None) or ((individual.count/individual.age) > (best.count/best.age)):
            best = individual
        
    return best
# def end tournament_selection

def mate_population(i1, i2):
    random.seed()
    b = brain.Brain(3,7,4)
    b.inputs[2] = 1
    b.hidden[6] = 1
    for i in xrange(3):
        for h in xrange(7):
            if random.random() <= 0.05:
                b.ih_weights[i][h] = random.uniform(-1.0,1.0)
            else:
                b.ih_weights[i][h] = random.choice([i1.brain.ih_weights[i][h],i2.brain.ih_weights[i][h]])
            
    for h in xrange(7):
        for o in xrange(4):
            if random.random() <= 0.05:
                b.ho_weights[h][o] = random.uniform(-1.0,1.0)
            else:
                b.ho_weights[h][o] = random.choice([i1.brain.ho_weights[h][o],i2.brain.ho_weights[h][o]])
                
    new_bug = bug.Bug(b, 100, 100, random.randint(1,10), random.randint(2,10), random.choice(['H']), random.choice(['M','F']), random.randint(1,5), 40)
    new_bug.set_goal([20,20])
    return new_bug
# end def mate_population

population = generate_population(100)

for i in xrange(1000):
    population = run_population(population, 100, 20, i)