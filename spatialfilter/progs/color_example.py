# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:14:42 2020

@author: sridevi
"""

import cv2



# opening the image and converting it to grayscale 
a = cv2.imread('../Figures/cir.png')
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)


cv2.imwrite('../Figures/color_ouptu.png', a)
