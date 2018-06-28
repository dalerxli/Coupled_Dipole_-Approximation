#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:16:44 2018

@author: renderer
"""

import matplotlib.pyplot as plt
import h5py
import numpy as np
import math as m
import os
import matplotlib as mpl


plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['font.size']=15

period=[100]
for per in period:
    wave=[]
    Qs=[]
    Qp=[]
    k=[]
    energy=[]
    AOI=[70,0,35,65,40,75,55,50,60,30,20,15,25,10,5,45]
    os.chdir('/home/renderer/Ievgen_stuff/Coupled_Dipole_-Approximation/Results/BG_sp90/S')
    files=os.listdir()
    for file in files:
        print(file)
        f=h5py.File(file,'r+')
        wave.append(list(f['wave']))
        Qs.append(list(f['q_ext']))
   
        f.close()
    
    
    os.chdir('/home/renderer/Ievgen_stuff/Coupled_Dipole_-Approximation/Results/BG_sp90/P')
    files=os.listdir()
    for file in files:
        print(file)
        f=h5py.File(file,'r+')
        
        Qp.append(list(f['q_ext']))
   
        f.close()
        
        
    for it,aoi in zip(wave,AOI):
        k.append([2*m.pi/x*m.sin(m.radians(aoi))/1e7 for x in it])
        energy.append([1240/x/1e9 for x in it])
    Q=[(np.asarray(Qs[i])+np.asarray(Qp[i]))/2 for i in range(len(Qs))]
    
    fig=plt.figure()
    cp = plt.contourf(k, energy, Q,500,vmin=0,vmax=5,cmap='jet')
    


    plt.xlabel(r'$K_{\parallel} (m^{-7})$',size=15)
    plt.ylabel('Energy (eV)',size=15)
    plt.suptitle('Extinction efficiency dispersion, period={}'.format(str(per)+'nm'), fontsize=15)
    cax = fig.add_axes([0.91, 0.15, 0.03, 0.7])
    cNorm = mpl.colors.Normalize(vmin=0,vmax=5)
    cb1 = mpl.colorbar.ColorbarBase(cax, norm=cNorm,cmap='jet')
    axes = plt.gca()
    plt.show()
