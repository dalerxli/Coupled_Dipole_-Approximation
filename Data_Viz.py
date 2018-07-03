# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:34:08 2018

@author: slimc
"""

import h5py
import matplotlib.pyplot as plt
import os
import numpy as np


Data=[]
R=[95,85,70,35,65,40,90,30,100,60,80,75,50,55,45]
d=os.chdir('Results/BG_15x15/S')
files=os.listdir(d)
for file in files:
    print(file)
    f = h5py.File(file, 'r')
    wave=f['wave']
    Q=f['q_ext']
    Q_sca=f['c_scat']
    
    wave=[i*1e9 for i in list(wave)]
    
    #plt.plot(wave,Q,label='')
    plt.plot(wave,Q_sca,label='c_scat')
    plt.xlabel('Wavelength (nm)')
    plt.xlim([min(wave),max(wave)])
    
    Data.append(Q)
    
#X,Y=np.meshgrid(wave,R)
#Data=np.asarray(Data).reshape(len(R),-1)
#plt.contourf(Y,X,Data,500,cmap='jet')
plt.legend()
plt.show()
