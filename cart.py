# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:57:12 2018

@author: BHARATH HEGDE
"""
import items as i

file=open("cart.txt","w")
file.write("ITEMS\t\tQUANTITY    UNIT PRICE\t AMOUNT\n")
file.close()

d=1
tcost=0
cost=0

while(d!=0):
    s=int(input("Select the category:\n1.Vegetables\n2.Fruits\n3.Milk Products\n"))
    if(s==1):
        name=input("Enter vegetable name:")
        q=int(input("Enter quantity:"))
        cost=i.veg(name,q)    
        
    elif(s==2):
        name=input("Enter fruit name:")
        q=int(input("Enter quantity:"))
        cost=i.fruits(name,q)
        
    elif(s==3):
        name=input("Enter milk product name:")
        q=int(input("Enter quantity:"))
        cost=i.milk(name,q)
        
    else:
        print("Select a vaild category\n")
    tcost=tcost+cost  
    d=int(input("Enter 0 if you want to exit, any other number to add another product:"))
    
i.unpack()

print("Total cost:\t\t\t\t ",tcost)