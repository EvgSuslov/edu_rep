# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:03:38 2022

fuel calculator 

@author: ruiny
"""

range_ = float(input('Расстояние до цели'+'\n'))
fuel_amaunt = float(input("рАСХОД НА 100"+'\n'))
fuel_cost = float(input('сТОЙМОСТЬ ЗА ЛИТР'+'\n'))
total = 0
if range_ > 0 and fuel_amaunt > 0 and fuel_cost > 0:
    total = ((fuel_amaunt / 100) * range_)  * fuel_cost
    
print('цена за поезлдку \n '+ str(total))