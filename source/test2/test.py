import bug
import sys
import time
import random

def display_grid(population, food, grid_size, count):
    grid = [['.' for col in xrange(grid_size)] for row in xrange(grid_size)]
    
    for i in population:
        grid[i.location[0]][i.location[1]] = 'B'
        
    for f in food:
        grid[f[0]][f[1]] = str(count)
        
    for row in grid:
        line = ''
        for column in row:
            line += column + ' '
        print line
# end def display_grid

def generate_population(pop_size, health, energy, max_size, max_legs, max_babies, grid_size):
    population = []
    
    for i in xrange(pop_size):
        random.seed(time.time())
        new_bug = bug.Bug(health, energy, random.randint(1,max_size), random.randint(2,max_legs), random.choice(['H']), random.choice(['M','F']), random.randint(1,max_babies), [39,39])
        population.append(new_bug)
    
    return population
# end def generate_population

population = generate_population(20, 100, 500, 10, 10, 2, 40)
food       = [[20,20],[8,3],[21,10],[9,6],[17,31],[24,0],[3,17],[38,38],[33,7],[11,30],[13,28],[20,27],[8,18]]

for i in population:
    i.set_brain(food[0])
    i.set_random_position(39)

def make_love(i1,i2,f):
    random.seed()
    new_bug = bug.Bug(100, 100, 2, 2, 2, 2, 2, [39,39])
    new_bug.set_brain(f)
    for i in xrange(2):
        for h in xrange(6):
            if random.random() <= 0.05:
                new_bug.ih_weights[i][h] = random.uniform(-1.0,1.0)
            else:
                new_bug.ih_weights[i][h] = random.choice([i1.ih_weights[i][h],i2.ih_weights[i][h]])
            
    for h in xrange(6):
        for o in xrange(4):
            if random.random() <= 0.05:
                new_bug.ho_weights[h][o] = random.uniform(-1.0,1.0)
            else:
                new_bug.ho_weights[h][o] = random.choice([i1.ho_weights[h][o],i2.ho_weights[h][o]])
                
    return new_bug

def evolve(population, food, p, f, sim_ann, epoch, tim):
    for i in population:
        i.set_food(f)
        #i.set_random_position(39)
    
    for t in xrange(100):
        count = 0
        for i in population:
            i.run_brain()
            if i.location[0] == f[0] and i.location[1] == f[1]:
                count += 1
        
        if tim != 0:
          sys.stderr.write("\x1b[2J\x1b[H")
          print 'Population Size: ' + str(len(population))
          print 'Generation: ' + str(epoch)
          print 'Individuals at Food: ' + str(count)
          print 'Annealing: ' + str(sim_ann)
          print
          display_grid(population, [f], 40, count)
          #time.sleep(tim)
        
    population = [i for i in population if (abs(i.location[0]-f[0]) <= sim_ann and abs(i.location[1]-f[1]) <= sim_ann)]
    
    while len(population) < p:
        random.seed()
        i1 = random.randint(0,(len(population)-1))
        i2 = random.randint(0,(len(population)-1))
        population.append(make_love(population[i1],population[i2],f))
    
    return population
    
sim_ann = 10
for i in xrange(100):
    t = 0.016666666667
    random.seed(time.time())
    food = [[random.randint(0,39),random.randint(0,39)]]
    f = food[0]
    if i != 0 and i%10 == 0 and sim_ann != 0:
        sim_ann -= 1
    if i >= 1000:
        t = 0.1
    population = evolve(population, food, 20, f, sim_ann, i, t)
    print i
    print sim_ann