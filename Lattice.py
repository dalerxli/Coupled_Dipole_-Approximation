import numpy as np
import math as m
from numpy.random import  uniform
import matplotlib.pyplot as plt

class Lattice:
    
    
    def __init__(self,nx=1,ny=1,step=100e-9,rx=20e-9,ry=20e-9,rz=20e-9):
        """
        Object initializer:
        
        Parameters:
            nx,ny--> amount of unit cells in x and y direction
            step--> lattice constant
            rx,ry,rz--> ellipsoid axes
        """
        self.type=None # Type of the lattice
        self.nx=nx # Amount of unit cells in x direction
        self.ny=ny # Amount of unit cells in x direction 
        self.step=step # Periodicity of the lattice
        self.rx=rx # X-axis radius of the nanoparticle
        self.ry=ry # Y-axis radius nanoparticle
        self.rz=rz # Z-axis radius nanoparticle
        self.N=nx*ny # Total number of used particles
        self.pos=np.zeros([self.N, 3]) # A vector of vectors , (x,y,z) positions
        self.r_eff=np.zeros([self.N,3]) # A vector with effective radius of each partic
    
    def Square(self):
        """
        A function to create a square lattice with the nx,ny unit cells, 
        lattice constant of step and particle dimension of rx,ry and rz.
                    
        Return:
            N--> total number of particles type(integer)
            pos--> position of each particle in the lattice type(numpy array)
            r_eff--> dimensions of each particle type(numpy array (1x3))
        """
        
       
        self.type="Square"
        # Assign the position coordinates and radius to each particle
        kk = 0
        for pos_i in np.arange(self.nx):
            for pos_j in np.arange(self.ny):
                self.pos[kk] = np.array([pos_i * self.step, pos_j * self.step, 0])
                self.r_eff[kk] = np.asarray([self.rx,self.ry,self.rz])
                kk += 1

        return self.N, self.pos, self.r_eff
    


    def Honeycomb(self):
        """
        A function to create a honeycomb lattice with the nx,ny unit cells, 
        lattice constant of step and particle dimension of rx,ry and rz.
                    
        Return:
            N--> total number of particles type(integer)
            pos--> position of each particle in the lattice type(numpy array)
            r_eff--> dimensions of each particle type(numpy array (1x3))
        """
    
    
        def latHC(a,N):
            latticeA=[(a,0,0),(-a/2,np.sqrt(3)/2*a,0),(-a/2,-np.sqrt(3)/2*a,0)]
            latticeB=[(-a,0,0),(a/2,-np.sqrt(3)/2*a,0),(a/2,np.sqrt(3)/2*a,0)]
            latticeA=np.array(latticeA)
            latticeB=np.array(latticeB)
        
            newA=[]
            newB=[]
            for elA,elB in zip(latticeA,latticeB):
                for i in range(0,int(N/2)):
                    for j in range(0,int(N/2)):
                    
                        
                        v3=(elA[0]+3*i*a,elA[1]+np.sqrt(3)*j*a,0)
                        v3m=(elA[0]-3*i*a,elA[1]-np.sqrt(3)*j*a,0)
                        v3mp=(elA[0]-3*i*a,elA[1]+np.sqrt(3)*j*a,0)
                        v3pm=(elA[0]+3*i*a,elA[1]-np.sqrt(3)*j*a,0)
                        if v3 not in newA:
                            newA.append(v3)
                        if v3m not in newA:
                            newA.append(v3m)
                        if v3mp not in newA:
                            newA.append(v3mp)
                        if v3pm not in newA:
                            newA.append(v3pm)
                        
                        v4=(elB[0]+3*i*a,elB[1]+np.sqrt(3)*j*a,0)
                        v4m=(elB[0]-3*i*a,elB[1]-np.sqrt(3)*j*a,0)
                        v4mp=(elB[0]-3*i*a,elB[1]+np.sqrt(3)*j*a,0)
                        v4pm=(elB[0]+3*i*a,elB[1]-np.sqrt(3)*j*a,0)
                        if v4 not in newB:
                            newB.append(v4)
                        if v4m not in newB:
                            newB.append(v4m)
                        if v4mp not in newB:
                            newB.append(v4mp)
                        if v4pm not in newB:
                            newB.append(v4pm)
            
            return list(set(newA))+ list(set(newB))
        
        self.pos=np.array(latHC(self.step,self.nx)) #Get the position array
        
        for k in range(len(self.r_eff)):
            self.r_eff[k]=np.asarray([self.rx,self.ry,self.rz])
        return self.N, self.pos, self.r_eff
    
    
    
    

    def Hexagonal(self):
        """
        A function to create a hexagonal lattice with the nx,ny unit cells, 
        lattice constant of step and particle dimension of rx,ry and rz.
                    
        Return:
            N--> total number of particles type(integer)
            pos--> position of each particle in the lattice type(numpy array)
            r_eff--> dimensions of each particle type(numpy array (1x3))
        """
    
        def latHex(a,N):
            a=a/m.sqrt(3)
            latticeA=[(a,0,0),(-a/2,m.sqrt(3)/2*a,0),(-a/2,-m.sqrt(3)/2*a,0)]
            latticeB=[(-a,0,0),(a/2,-m.sqrt(3)/2*a,0),(a/2,m.sqrt(3)/2*a,0)]
            latticeA=np.array(latticeA)
            latticeB=np.array(latticeB)
    
            newA=[]
            newB=[]
            for elA,elB in zip(latticeA,latticeB):
                for i in range(0,int(N/2)):
                    for j in range(0,int(N/2)):
                
                    
                        v3=(elA[0]+3*i*a,elA[1]+m.sqrt(3)*j*a,0)
                        v3m=(elA[0]-3*i*a,elA[1]-m.sqrt(3)*j*a,0)
                        v3mp=(elA[0]-3*i*a,elA[1]+m.sqrt(3)*j*a,0)
                        v3pm=(elA[0]+3*i*a,elA[1]-m.sqrt(3)*j*a,0)
                        if v3 not in newA:
                            newA.append(v3)
                        if v3m not in newA:
                            newA.append(v3m)
                        if v3mp not in newA:
                            newA.append(v3mp)
                        if v3pm not in newA:
                            newA.append(v3pm)
                    
                        v4=(elB[0]+3*i*a,elB[1]+m.sqrt(3)*j*a,0)
                        v4m=(elB[0]-3*i*a,elB[1]-m.sqrt(3)*j*a,0)
                        v4mp=(elB[0]-3*i*a,elB[1]+m.sqrt(3)*j*a,0)
                        v4pm=(elB[0]+3*i*a,elB[1]-m.sqrt(3)*j*a,0)
                        if v4 not in newB:
                            newB.append(v4)
                        if v4m not in newB:
                            newB.append(v4m)
                        if v4mp not in newB:
                            newB.append(v4mp)
                        if v4pm not in newB:
                            newB.append(v4pm)
        
            return list(set(newB))
    
        self.pos=np.array(latHex(self.step,self.nx))
        self.N=len(self.pos)
    
    
        # Creates a effective radius vector
        self.r_eff = np.zeros([self.N]) # A vector with effective radius of each particle
        for k in range(len(self.r_eff)):
            self.r_eff[k]=self.rx
        return self.N, self.pos, self.r_eff
    
    
    
    def Random(self,N=10, x_span=100E-9, y_span=100E-9,z_span=40E-9, max_radius = 10E-9, min_radius = 2E-9):
        """
        A function to create random position lattice with the random size from min_radius to max_radius.
                    
        Return:
            N--> total number of particles type(integer)
            pos--> position of each particle in the lattice type(numpy array)
            r_eff--> dimensions of each particle type(numpy array (1x3))
        """
        assert (4/3)*np.pi*max_radius**3 <= x_span*y_span*z_span # Make sure the volume of the box is larger than the volume of the largest sphere
        self.pos = np.zeros([N, 3]) # A vector of vector (x,y,z) positions
        self.r_eff = np.zeros([N]) # A vector with effective radius of each particle

        # calcualtes the distance between two spheres
        def distance (pos_1,pos_2):
            temp = pos_2-pos_1
            return np.sqrt(temp[0]**2 + temp[1]**2 +temp[2]**2)

        i = 0
        while (i < N):
            #Create a position and radius that is uniformly distributed
            self.pos[i] = uniform(low =0, high = 1, size = 3)* np.array([x_span, y_span, z_span])
            self.r_eff[i] = uniform(low =min_radius/max_radius, high = 1, size = 1)* max_radius
            # Lets check if the distance between the current sphere and all other spheres is less than the sum of radius of the current sphere and all other spheres
            for j in range(i):
                if (distance(self.pos[j],self.pos[i]) < 1*(self.r_eff [i]+self.r_eff [j])) :
                    print (distance(self.pos[j],self.pos[i]), 1*(self.r_eff [i]+self.r_eff [j]))
                    print ('Collision with other sphere detected. Removing this sphere')
                    i=i-1 # Lets remove this guy and start our again
                    break

            i+=1

        return self.N, self.pos, self.r_eff
    
    
    def Grid_Viz(self):
        """
        A function which displays position of nanoparticles, the complete Lattice
        Return:
            A figure of a lattice
        """
        plt.figure('Grid')
        plt.scatter([i[0]*1e6 for i in self.pos],[i[1]*1e6 for i in self.pos])
        plt.xlabel('X (um)')
        plt.ylabel('Y (um)')
        plt.show()
        return