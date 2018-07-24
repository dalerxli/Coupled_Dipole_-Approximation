#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:06:35 2018

@author: renderer
"""

import os 
import matplotlib.pyplot as plt
import re

d={}
colors=['r','g','b','k']
with open('/home/renderer/Ievgen_stuff/MPB/BG_last/BG-tm.dat','r') as f:
    for line in f:
        line=re.split(r', ',line)
        print(line)
        if 'k index' in line:
            continue
        else:
            k=float(line[1])
            if k not in d.keys():
                d[k]={}
                d[k]['b1']=[]
                d[k]['b2']=[]
                d[k]['b3']=[]
                d[k]['b4']=[]
            d[k]['b1'].append(float(line[6]))
            d[k]['b2'].append(float(line[7]))
            d[k]['b3'].append(float(line[8]))
            d[k]['b4'].append(float(line[9]))
            
for k in d.keys():
    for band in d[k].keys():
        col=colors[list(d[k].keys()).index(band)]
        plt.scatter(k,d[k][band][0],c=col)
plt.show()
            