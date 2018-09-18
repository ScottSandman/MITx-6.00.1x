# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:59:53 2018

@author: Sandman
"""
aDict = {33:1, 2:2, 333:33, 4:52, 45:33}
target = 33

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    L = []
    for k in aDict:
        if aDict[k] == target:
            L.append(k)
    L.sort()
    return L

print(keysWithValue(aDict, target))