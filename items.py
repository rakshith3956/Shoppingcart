# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:55:27 2018

@author: BHARATH HEGDE
"""


def pack(name,qu,cost):
        c=str(cost)
        amount=cost*qu
        a=str(amount)
        q=str(qu)
        file=open("cart.txt","a")
        t=name+"\t\t  "+q+"\t\t"+c+"\t  "+a+"\n"
        file.write(t)
        file.close()
        
def unpack():
        print("Your cart:\n")
        with open("cart.txt","r") as file:
            for line in file:
                print(line)
        
def veg(name,q):
    if(name=='tomato'):
        cost=25
        pack(name,q,cost)
        return cost
        
        
    elif(name=='onion'):
        cost=30
        pack(name,q,cost)
        return cost
    
    elif(name=='potato'):
        cost=30
        pack(name,q,cost)
        return cost
    
    else:
        print("Item not available")
        return 0
        
def fruits(name,q):
    if(name=='apple'):
        cost=150
        pack(name,q,cost)
        return cost
        
    elif(name=='mango'):
        cost=90
        pack(name,q,cost)
        return cost
    
    elif(name=='orange'):
        cost=60
        pack(name,q,cost)
        return cost
    else:
        print("Item not available")
        return 0
    
def milk(name,q):
    if(name=='milk'):
        cost=40
        pack(name,q,cost)
        return cost
    
        
    elif(name=='curds'):
        cost=40
        pack(name,q,cost)
        return cost
    
    elif(name=='lassi'):
        cost=20
        pack(name,q,cost)
        return cost
    else:
        print("Item not available")
        return 0


    