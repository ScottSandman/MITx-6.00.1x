# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:52:36 2018

@author: Sandman
"""
L = [[1, 2], [3, 4], [5, 6, 7]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for i in range(len(L)):
        index = L[i]
        index.reverse()

deep_reverse(L)
print(L)
      