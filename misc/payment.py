# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ccbalance(balance, annualInterestRate):
    ''' use a starting balance and annual interest rate to 
    calculate lowest monthly payment to pay a credit card balance within
    one year.
    
    arguments
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    '''
    count = 1
    pymt = 10 #starting monthly payment amount
    newbal = balance
    
    while newbal > 0:
        if newbal == 0 and count <= 12:
            break
        if newbal != 0 and count > 12: #reset loop variables
            count = 1
            newbal = balance
            pymt += 10
#           print('payment: ', pymt)
            continue
        unbal = newbal - pymt #calculate new unpaid balance
        mint = annualInterestRate / 12 #calculate monthly interest rate
        newbal = unbal + unbal * mint #calculate updated balance
        count += 1
        
    print('Lowest Payment: ', pymt)  
            

            
                
    
 #  print('Remaing Balance: ', round(balance,2))     
        
 # if count <= 13:
 #       if count > 12:
 #           print('Remaing Balance: ', round(balance,2))  
    
    
        
         

    