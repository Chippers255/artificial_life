import bug
import math
import brain
import random

MUTATION_CHANCE = 0.01

def tournament_distance_selection(population, tournament_size):
    global MUTATION_CHANCE

    random.seed()
    
    length = len(population) - 1
    mate_1 = population[random.randint(0,length)]
    mate_2 = population[random.randint(0,length)]
    
    for i in xrange(tournament_size):
        individual_1 = population[random.randint(0,length)]
        individual_2 = population[random.randint(0,length)]
        
        distance_1 = ((individual_1.goal[0] - individual_1.location[0])**2) + ((individual_1.goal[1] - individual_1.location[1])**2)
        distance_2 = ((individual_2.goal[0] - individual_2.location[0])**2) + ((individual_2.goal[1] - individual_2.location[1])**2)
        distance_3 = ((mate_1.goal[0] - mate_1.location[0])**2) + ((mate_1.goal[1] - mate_1.location[1])**2)
        distance_4 = ((mate_2.goal[0] - mate_2.location[0])**2) + ((mate_2.goal[1] - mate_2.location[1])**2)
        
        distance_1 = math.sqrt(distance_1) - individual_1.count
        distance_2 = math.sqrt(distance_2) - individual_2.count
        distance_3 = math.sqrt(distance_3) - mate_1.count
        distance_4 = math.sqrt(distance_4) - mate_2.count
        
        if distance_1 < distance_3:
            mate_1 = individual_1
        
        if distance_2 < distance_4:
            mate_2 = individual_2
    
    return mate_1.procreate(mate_2, MUTATION_CHANCE)
# end def tournament_selection


def tournament_count_selection(population, tournament_size):
    global MUTATION_CHANCE

    random.seed()
    
    length = len(population) - 1
    mate_1 = population[random.randint(0,length)]
    mate_2 = population[random.randint(0,length)]
    
    for i in xrange(tournament_size):
        individual_1 = population[random.randint(0,length)]
        individual_2 = population[random.randint(0,length)]
        
        distance_1 = individual_1.count
        distance_2 = individual_2.count
        distance_3 = mate_1.count
        distance_4 = mate_2.count
        
        if distance_1 < distance_3:
            mate_1 = individual_1
        
        if distance_2 < distance_4:
            mate_2 = individual_2
    
    return mate_1.procreate(mate_2, MUTATION_CHANCE)
# end def tournament_selection


def average_distance_selection(population):
    global MUTATION_CHANCE

    random.seed()
    
    population_average = 0
    length             = len(population)

    for i in population:
        distance = ((i.goal[0] - i.location[0])**2) + ((i.goal[1] - i.location[1])**2)
        population_average += math.sqrt(distance) - i.count
    population_average /= length
    
    while True:
        mate_1 = population[random.randint(0,length-1)]
        mate_2 = population[random.randint(0,length-1)]

        distance_1 = ((mate_1.goal[0] - mate_1.location[0])**2) + ((mate_1.goal[1] - mate_1.location[1])**2)
        distance_2 = ((mate_2.goal[0] - mate_2.location[0])**2) + ((mate_2.goal[1] - mate_2.location[1])**2)

        distance_1 = math.sqrt(distance_1) - mate_1.count
        distance_2 = math.sqrt(distance_2) - mate_2.count

        if distance_1 <= population_average and distance_2 <= population_average:
            return mate_1.procreate(mate_2, MUTATION_CHANCE)
# end def average_selection

def average_count_selection(population):
    global MUTATION_CHANCE

    random.seed()
    
    population_average = 0
    length             = len(population)

    for i in population:
        population_average += i.count
    population_average /= length
    
    while True:
        mate_1 = population[random.randint(0,length-1)]
        mate_2 = population[random.randint(0,length-1)]

        distance_1 = mate_1.count
        distance_2 = mate_2.count

        if distance_1 <= population_average and distance_2 <= population_average:
            return mate_1.procreate(mate_2, MUTATION_CHANCE)
# end def average_selection


def random_selection(popultion):
    global MUTATION_CHANCE

    random.seed()
    
    mate_1 = population[random.randint(0,len(population)-1)]
    mate_2 = population[random.randint(0,len(population)-1)]

    return mate_1.procreate(mate_2, MUTATION_CHANCE)
# end def random_selection