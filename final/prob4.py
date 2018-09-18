# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:55:15 2018

@author: Sandman
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) and len(L2) == 0:
        ans = (None, None, None)
        return ans
    if len(L1) != len(L2):
        return False
    for i in L1:
        if i not in L2:
            return False
    L1_dict = {}
    L2_dict = {}
    for char in L1:
        if char in L1_dict:
            L1_dict[char] += 1
        else:
            L1_dict[char] = 1
    for char in L2:
        if char in L2_dict:
            L2_dict[char] += 1
        else:
            L2_dict[char] = 1
    for k in L1_dict:
        if L1_dict.get(k) != L2_dict.get(k):
            return False
            
    values = L1_dict.values()
    best = max(values)
    for k in L1_dict:
        if L1_dict[k] == best:
            s1 = k
            s2 = best
            s3 = type(k)
    solution = (s1, s2, s3)
    return solution
                
    
        
            