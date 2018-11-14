# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:52:24 2018

@author: edup_
"""

from Utils import functions
from Data import triangles

for dictionary in triangles.triangle_definitions:
        print(functions.area_triangle(dictionary["base"], dictionary["height"]))