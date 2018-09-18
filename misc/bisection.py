# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ccbalance(balance, annualInterestRate):
    ''' use a starting balance and annual interest rate to 
    calculate lowest monthly payment to pay a credit card balance within
    one year utilizing a bisection approach.
    
    arguments
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    '''
       
    count = 1
    mint = annualInterestRate / 12 #calculate monthly interest rate
    low = balance / 12 #lower bound for payment
    high = (balance * (1 + mint)**12) / 12.0 #higher bound for payment
    newbal = balance
    
    while newbal != 0:
        pymt = round((low + high) / 2, 4) #starting monthly payment amount
        while count <= 12: #iterate for num of months
            unbal = newbal - pymt #calculate new unpaid balance
            newbal = round(unbal + unbal * mint, 4) #calculate updated balance
            count += 1
        if abs(newbal) < 0.01:
            break
        if newbal > 0:
            count = 1
            newbal = balance
            low = pymt
            continue
        else:
            high = pymt
            count = 1
            newbal = balance
            continue
        
        
    print('Lowest Payment: ', round(pymt, 2))  
            

            
                
    
 #  print('Remaing Balance: ', round(balance,2))     
        
 # if count <= 13:
 #       if count > 12:
 #           print('Remaing Balance: ', round(balance,2))  
    
    
        
         

    