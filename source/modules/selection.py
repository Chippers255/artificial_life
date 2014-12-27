import bug
import brain
import random


def tournament_selection(population, tournament_faction_size):
    random.seed()
    
    tournament_size = int(len(population) / tournament_fraction_size)
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
# end def tournament_selection


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