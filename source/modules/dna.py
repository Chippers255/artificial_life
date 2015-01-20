# -*- coding: utf-8 -*-

# dna.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
# Created..........................2015-01-12
# Modified.........................2015-01-20
#
# This module contains the dna class and was developed for use in the Bugs
# project.

import time
import random

class DNA(object):
    """The DNA class is designed to hold all genetic material required for
    creating a bug. Each bug DNA contains 9 chromosomes for different traits
    for a bug. Each chromosome contains a list of genes and each gene has
    2 alleles. For bug DNA '0' was chosen to be the dominant allele for each
    gene and '1' was chosen to be recessive. A phenotype is chosen by anding
    the two allele together.
    
    The Following is a list of chromosomes and their relative trait.
    
    c0: Bug Size
    c1: Bug Gender
    c2: Number of Offspring
    c3: Food consumption type
    c4: Number of Eyes
    c5: Distance for vision
    c6: Distance for smell
    c7: Individual bug smell

    c8: Weight matrix for brain between input and hidden layer
    c9: Weight matric for brain between hidden and output layer
    
    """
    
    def __init__(self, dna, brain_i, brain_h, brain_o):
        """This method will initialize a new dna sequence with two
        possibilities. First a DNA sequence can be passed as an argument when
        reproduction occurs. Secondly if no DNA sequence is pass ed then a
        randomized DNA will be created, usually for initialization of bugs.

        :param dna:     A precreated list of genes (usually from mating)
        :param brain_i: Size of input layer for the brain
        :param brain_h: Size of hidden layer for the brain
        :param brain_o: Size of output layer for the brain
        
        :return: NaN
        
        """
        random.seed(time.time())
        
        if dna == None:
            self.c0 = [[random.randint(0,1) for a in xrange(2)] for g in xrange(2)] # Bug Size
            self.c1 = [[random.randint(0,1) for a in xrange(2)] for g in xrange(1)] # Bug Gender
            self.c2 = [[random.randint(0,1) for a in xrange(2)] for g in xrange(3)] # Bug Offspring
            self.c3 = [[random.randint(0,1) for a in xrange(2)] for g in xrange(2)] # Bug Food
            self.c4 = [[random.randint(0,1) for a in xrange(2)] for g in xrange(3)] # Num Eyes
            self.c5 = [[random.randint(0,1) for a in xrange(2)] for g in xrange(2)] # sight distance
            self.c6 = [[random.randint(0,1) for a in xrange(2)] for g in xrange(4)] # olfactory distance
            self.c7 = [[random.randint(0,1) for a in xrange(2)] for g in xrange(9)] # personal smell
            self.c8 = [[random.uniform(-1,1) for h in xrange(move_h)] for i in xrange(move_i)] # movement brain i_h
            self.c9 = [[random.uniform(-1,1) for o in xrange(move_o)] for h in xrange(move_h)] # movement brain h_o
        else:
            self.c0 = dna[0]
            self.c1 = dna[1]
            self.c2 = dna[2]
            self.c3 = dna[3]
            self.c4 = dna[4]
            self.c5 = dna[5]
            self.c6 = dna[6]
            self.c7 = dna[7]
            self.c8 = dna[8]
            self.c9 = dna[9]
    # end def __init__
    
    def bin_dec(self, chromosome):
        """This method will convert a chromosome into a decimale value
        for use in bug creation. 
        
        :param chromosome: A Chromosome in 2-pair list form
        
        :return: Integer value for a chromosome
        
        """
        trait = ''
        for gene in chromosome:
            trait += str(gene[0] & gene[1])
        return int(trait, 2)
    # end def bin_dec
    
    def get_size(self):
        return self.bin_dec(self.c0)
    # end def get_size
    
    def get_gender(self):
        return self.bin_dec(self.c1)
    # end def get_gender
    
    def get_offspring(self):
        return self.bin_dec(self.c2)
    # end def get_offspring
    
    def get_food(self):
        return self.bin_dec(self.c3)
    # end def get_food
    
    def get_eyes(self):
        return self.bin_dec(self.c4)
    # end def get_size
    
    def get_perception(self):
        return self.bin_dec(self.c5)
    # end def get_gender
    
    def get_smell(self):
        return self.bin_dec(self.c6)
    # end def get_offspring
    
    def get_odour(self):
        return self.bin_dec(self.c7)
    # end def get_offspring
    
    def print_dna(self):
        print "C0: " + str(self.c0)
        print "Size: " + str(self.get_size())
        print
        print "C1: " + str(self.c1)
        print "Gender: " + str(self.get_gender())
        print
        print "C2: " + str(self.c2)
        print "Offspring: " + str(self.get_offspring())
        print
        print "C3: " + str(self.c3)
        print "Food: " + str(self.get_food())
        print
        print "C4: " + str(self.c4)
        print "Eyes: " + str(self.get_eyes())
        print
        print "C5: " + str(self.c5)
        print "Perception: " + str(self.get_perception())
        print
        print "C6: " + str(self.c6)
        print "Smell: " + str(self.get_smell())
        print
        print "C7: " + str(self.c7)
        print "Odour: " + str(self.get_odour())
        print
    # end def print_dna
    
# end class DNA
