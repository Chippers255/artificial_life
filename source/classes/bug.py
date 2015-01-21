# -*- coding: utf-8 -*-

# bug.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
# Created..........................2015-01-10
# Modified.........................2015-01-20
#
# This module contains the bug class and was developed for use in the Bugs
# project.

import dna
import time
import math
import random


class Bug(object):
    """The bug class is used to represent a single bug. Each bug will have a
    series of qualities that are randomly assigned unless provided. This class
    contains a series of functions so a bug may make decisions and perform a
    variety of actions.

    """

    def __init__(self, in_dna, in_health, in_hunger, in_location):
        """


        :type in_location: [int,int]
        :type in_dna: DNA object

        """
        random.seed(time.time())

        self.dna      = in_dna
        self.health   = in_health
        self.hunger   = in_hunger
        self.location = in_location

        self.size       = self.dna.get_size()
        self.gender     = self.dna.get_gender()
        self.offspring  = self.dna.get_offspring()
        self.food       = self.dna.get_food()
        self.eyes       = self.get_eyes()
        self.perception = self.get_perception()
        self.smell      = self.dna.get_smell()
        self.odour      = self.get_odour()

        self.count    = 0
        self.age      = 0
        self.children = 0

        self.set_eyes()
        self.set_brain()
    # end def __init__

    def train_bug(self):
        return True
    # end def train_bug

    def run_bug(self):
        return True
    # end def run_bug

    def attack_move(self, other_bug):
        return True
    # end def attack_move

    def mate_move(self, other_bug, mutation):
        return True
    # end def mate_move

    def walk_move(self):
        return True
    # end def walk_move

    def run_move(self):
        return True
    # end def run_move

    def no_move(self):
        return True
    # end def no_move

    def set_eyes(self):
        return True
    # end def set_eyes

    def set_brain(self):
        return True
    # end def set_brain

    def print_bug(self):
        return True
    # end def print_bug
    
# end class Bug