# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:51:37 2017

@author: Ievgen Voloshenko
"""

import os
import h5py
import math as m
import matplotlib.pyplot as plt
import re
import matplotlib as mpl

def DO(lc,AOI,n,N_m):
    lc=2*m.pi/lc
    a=1
    b=-(2*m.sin(m.radians(AOI))*lc)/(N_m**2-m.sin(m.radians(AOI))*m.sin(m.radians(AOI)))
    c=-lc**2/(N_m**2-m.sin(m.radians(AOI))*m.sin(m.radians(AOI)))
    
    d=b**2-4*a*c
    
    x=(-b+m.sqrt(d))/(2*a)
    return x
    
    


period=[180]

plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['font.size']=10
for per in period:
    wave=[]
    Q=[]
    k=[]
    energy=[]
    AOI=[65,30,15,70,25,35,10,5,40,55,45,60,50,0,75,20]
    os.chdir('/home/renderer/Ievgen_stuff/Coupled_Dipole_-Approximation/Results/Betta_Graphyne_new/0')
    files=os.listdir()
    for file in files:
        print(file)
        f=h5py.File(file,'r+')
        wave.append(list(f['wave']))
        Q.append(list(f['q_ext']))
   
        f.close()
    
    for it,aoi in zip(wave,AOI):
        k.append([2*m.pi/x*m.sin(m.radians(aoi))/1e7 for x in it])
        energy.append([1240/x/1e9 for x in it])

    kdo=[DO(360e-9,aoi,1,1.52) for aoi in AOI]
    #plt.plot(kdo,[x*2*m.pi/1240 for x in kdo],'w--')
    fig=plt.figure()
    cp = plt.contourf(k, energy, Q,500,cmap='jet')
    #plt.plot(kdo,[1240/(2*m.pi/x*1e9) for x in kdo],'w--')


    plt.xlabel(r'$K_{\parallel} (m^{-7})$',size=15)
    plt.ylabel('Energy (eV)',size=15)
    plt.suptitle('Extinction efficiency dispersion, period={}'.format(str(per)+'nm'), fontsize=15)
    cax = fig.add_axes([0.91, 0.15, 0.03, 0.7])
    cNorm = mpl.colors.Normalize()
    cb1 = mpl.colorbar.ColorbarBase(cax, norm=cNorm,cmap='jet')
    axes = plt.gca()
    plt.show()
    #os.chdir('C:\\Users\\Ievgen Voloshenko\\Desktop\\CDA_PYTHON-master\\Parameters search\\HC\\results')
    #plt.savefig('{}nm.png'.format(str(per)),dpi=600)
    #plt.close()

   
    




