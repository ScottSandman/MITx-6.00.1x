# -*- coding: utf-8 -*-
"""
Created on Wed May  2 14:46:07 2018

@author: Sandman
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. 
    """
    #create blank dict for solution
    key_code = {}
    
    #append dictionary keys:values
    count = 0
    for char in map_from:
        key_code[char] = map_to[count]
        count += 1
#    return key_code
    #decode "code"
    decoded = ''
    for char in code:
        decoded += key_code.get(char)
#        print(decoded)
    #return tuple with dict and decode
    solution = (key_code, decoded)
    return solution