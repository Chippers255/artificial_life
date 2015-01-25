# -*- coding: utf-8 -*-

"""Class for creating a working with Bug DNA and genetics."""

# math_tools.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
# Created..........................2015-01-25
# Modified.........................2015-01-25
#
# This module contains the dna class and was developed for use in the Bugs
# project.
#
# Copyright (C) 2015 Thomas Nelson


def bin_dec(chromosome):
    """This method will convert a chromosome into a decimal value
    for use in bug creation.

    :param chromosome: A Chromosome in 2-pair list form

    :return: Integer value for a chromosome

    """

    trait = ''

    for gene in chromosome:
        trait += str(gene[0] & gene[1])

    return int(trait, 2)
# end def bin_dec

