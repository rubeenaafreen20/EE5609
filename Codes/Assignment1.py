# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 02:50:49 2020

@author: Rubeena
"""


import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #Taken from Dr. GVV Sharma's github

#Line points
P = np.array([1,2]) 
Q = np.array([5,3]) 
M = np.array([2.6,0])  #thepoint on x-axis where reflection takes place

slope_PM=(M[1]-P[1])/(M[0]-P[0]) #check the slope of incident ray
slope_QM=(M[1]-Q[1])/(M[0]-Q[0]) #check the slope of reflected ray

print(slope_PM)
print("\n")
print(slope_QM)

#Draw figure for reflection

x_PM=line_gen(P,M)
plt.plot(x_PM[0,:],x_PM[1,:],label="PM")

x_QM=line_gen(Q,M)
plt.plot(x_QM[0,:],x_QM[1,:],label="QM")

#plotting and labelling of points
plt.plot(P[0], P[1], '.')
plt.text(P[0] * (1 + 0.1), P[1] * (1 + 0.1) , 'P(1,2)')
plt.plot(Q[0], Q[1], '.')
plt.text(Q[0] * (1 -0.06), Q[1] * (1+0.05) , 'Q(5,3)')
plt.plot(M[0], M[1], '.')
plt.text(M[0] * (1 + 0.1), M[1] * (1 - 0.1) , 'M(13/5,0)')

plt.grid()
plt.xlim(0, 6)
plt.ylim(-1, 6)
