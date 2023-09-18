#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:45:14 2023

@author: dai
"""

def f(a=23,b=2,c=3,*tup,**kwarg):
    print(a)
    print(b)
    print(c)
    print(tup)
    print(kwarg)
    
    s=a+b+c
    
    for d in tup:
        s=s+d
    for k in kwarg.values():
        s=s+k
    return s

print("Sum= ", f(1,2,3))
print("Sum = ", f(1,2,3,4,5,6,7,8,x=9,y=11,z=12))