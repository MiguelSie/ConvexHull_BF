# -*- coding: utf-8 -*-
"""Convex Hull BF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sc_duQYctNiao7EjTntMxQQsUqrR7cEt
"""

from numpy import array
from numpy import linspace
import matplotlib as mpl
from matplotlib import pyplot as plt
import math

def leqt(x1, x2, y1, y2, sw):
  if (sw != True):
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - ( (y2 - y1) / (x2 - x1) ) * x1
    return lambda x: slope * x + intercept
  else:
    return lambda x: x1-x

#Ps = [(1,6), (4, 15), (7,7), (10, 13), (11, 6), (11, 18), (11, 21), (12, 10), (15, 18), (16, 6), (18, 3), (18, 12), (19, 15), (22, 19)]
Ps = [(13, 0), (-6, -12), (15, -14), (5, -2), (-3, 9), (14, -10), (-8, 4), (11, 10), (-13, 6), (2, -15), (-1, -9), (7, 3), (-4, 12)]
P = []
ms = []
equations = []
exs = []
angles = []

for i in range (len(Ps)-1):
  for j in range (i+1, len(Ps)):
    sw2 = False
    y2 = Ps[j][1]
    y1 = Ps[i][1]
    x1 = Ps[i][0]
    x2 = Ps[j][0]
    if (x2-x1==0):
      sw2=True
    else:
      m=(y2-y1)/(x2-x1)
      n=y1-m*x1
    res = []

    for k in range (len(Ps)):
      xk = Ps[k][0]
      yk = Ps[k][1]
      if (sw2 != True):
        eq = yk - m*xk - n
      else:
        eq = x1-xk
      res.append(eq)
      sw = 1
      
    if (res[0]<=0):
      ii = 0
      while(sw == 1 and ii < len(res)):
        if (res[ii] > 0):
          sw = 0
        ii = ii+1
      if (sw == 1):
        P.append(((Ps[i][0], Ps[i][1]), (Ps[j][0], Ps[j][1]))) 
        equations.append(leqt(x1, x2, y1, y2, sw2))
        exs.append(linspace(x1, x2, 256))
        ms.append(m)
        print("y = "+str(m)+"x + "+str(n))
    sw = 1
    if (res[0]>=0):
      ii = 0
      while(sw == 1 and ii < len(res)):
        if (res[ii] < 0):
          sw = 0
        ii = ii+1
      if (sw == 1): 
        P.append(((Ps[i][0], Ps[i][1]), (Ps[j][0], Ps[j][1])))
        equations.append(leqt(x1, x2, y1, y2, sw2))
        exs.append(linspace(x1, x2, 256))
        ms.append(m)
        print("y = "+str(m)+"x + "+str(n))

fig, ax = plt.subplots()
for i in range(len(equations)):
  x = exs[i]
  y = equations[i](x)
  ax.plot(x, y, color='black')

ps = array(Ps)
xi, yi = ps[:, 0], ps[:, 1]
ax.plot(xi, yi, linestyle='', color='red', marker='*', markersize=12)

print(P)

for i in range(len(P)-1):
  for j in range(i+1, len(P)):
    if (P[i][0] == P[j][0] or P[i][0] == P[j][1] or P[i][1] == P[j][0] or P[i][1] == P[j][1]):
      aux = (ms[i] - ms[j]) / (1+ ms[i]*ms[j])
      angles.append(math.degrees(math.atan(aux)))
print(angles)

#Deber??a dar 128.571428571429