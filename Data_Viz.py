# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:34:08 2018

@author: slimc
"""

import h5py
import matplotlib.pyplot as plt
import os

f = h5py.File('Betta_Graphyne 0.0 0.0.hdf5', 'r')
wave=f['wave']
Q=f['q_ext']
Q_sca=f['q_scat']

wave=[i*1e9 for i in list(wave)]

plt.plot(wave,Q,label='Q_ext')
plt.plot(wave,Q_sca,label='Q_scat')
plt.xlabel('Wavelength (nm)')
plt.xlim([min(wave),max(wave)])
plt.legend()