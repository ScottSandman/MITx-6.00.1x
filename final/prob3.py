# -*- coding: utf-8 -*-
"""
Created on Wed May  2 10:46:36 2018

@author: Sandman
"""

def sum_digits(s):
    """ assumes s a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s it raises a ValueError exception.
    """
    total = 0
    for i in s:
        if i in "1234567890":
            total += int(i)
    if total == 0:
        raise ValueError("string did not contain digits")
            
    return total
          