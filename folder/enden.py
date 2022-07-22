# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 15:10:39 2022

@author: ruiny
"""

for x in range(1, 100):
    if x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:
        print(x) 