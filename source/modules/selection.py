import bug
import brain
import random


def tournament_distance_selection(population, tournament_size):
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
    
    new_bug = mate_1.procreate(mate_2, 0.01)
    
    return new_bug
# end def tournament_selection

def tournament_count_selection(population, tournament_size):


def average_selection(population):
    random.seed()
    
    population_average = 0
    for i in xrange(len(population)):
        distance = ((i.goal[0] - i.location[0])**2) + ((i.goal[1] - i.location[1])**2)
        population_average += math.sqrt(distance) - i.count
    population_average /= len(population)
    
    while True:
        individual = population[random.randint(0,len(population)-1)]
        distance   = ((individual.goal[0] - individual.location[0])**2) + ((individual.goal[1] - individual.location[1])**2)
        distance   = math.sqrt(distance) - individual.count
        if distance < population_average:
            return individual
# end def average_selection


def random_selection(popultion):
    random.seed()
    
    return population[random.randint(0,len(population)-1)]
# end def random_selection