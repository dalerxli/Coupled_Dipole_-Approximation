#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:03:19 2018

@author: renderer
"""
import os 

with open('args.txt','w') as f:

    for aoi in range(0,80,5):
        wvl_min=300e-9
        wvl_max=1100e-9
        wvl_step=3e-9
        tol=10e-5
        rx=30e-9        
        ry=rx
        rz=0.8*rx
        AOI=aoi
        Phi=0
        mat='Au'
        Nm=1.25
        nx=5
        ny=5
        space=rx*3
        Lat='Betta_Graphyne'
        sd='home/Ievgen_stuff/Coupled_Dipole_-Approximation/Results '
        
        f.write('python3 CDA.py {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}\n'.format(wvl_min,wvl_max,wvl_step,tol,rx,ry,rz,aoi,Phi,mat,Nm,nx,ny,space,Lat,sd))
