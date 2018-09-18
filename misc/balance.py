# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ccbalance(balance, annualInterestRate, monthlyPaymentRate):
    ''' use a starting balance, annual interest rate and monthly
    payment rate to caculate a credit card balance at the end of
    one year.
    
    arguments
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal
    '''
    count = 1
    while count <= 13:
        if count > 12:
            print('Remaing Balance: ', round(balance,2))
        mpay = balance * monthlyPaymentRate #calculate minimum payment
        unbal = balance - mpay #calculate new unpaid balance
        mint = annualInterestRate / 12 #calculate monthly interest rate
        balance = unbal + unbal * mint #calculate updated balance
        count += 1
    
        
        
cc = ccbalance(1000, 0.03, 0.2)
print(cc)    
    
    
        
         

    