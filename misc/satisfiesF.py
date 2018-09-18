# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:14:14 2018

@author: Sandman
"""

L = ['a', 'ab', 'a']

def f(s):
    return 'ab' in s

    
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a
        Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
        that f(s) returns True, and no other elements. Remaining elements in L
        should be in the same order.
    Returns the length of L after mutation
    """
    copy_L = L[:]
    for s in copy_L:
        if f(s) == False:
            L.remove(s)
    return (len(L))

print(satisfiesF(L))

            