from __future__ import division
import numpy as np
from numpy import random
import costFunc as cF   


class Particle(object):
    count = 0
    def __init__(self,dims,num_func,bounds,optimize):
        self.num_func = num_func
        self.position_i=random.uniform(bounds[0],bounds[1],size = (dims))          # particle position
        self.velocity_i=np.zeros((dims))         # particle velocity
        self.pos_best_i= self.position_i.copy()         # best position individual
        self.err_best_i=-1          # best error individual
        self.err_i=-1               # error individual
        self.pos_best_neighbor_i = self.position_i.copy() 
        self.err_best_neighbor_i = -1
        self.dims = dims
        self.optimize = optimize
    def evaluate(self,count):
        Particle.count += count
        self.err_i=cF.costFunc(self.num_func,self.position_i,self.dims)
        if abs(self.err_i-self.optimize)<abs(self.err_best_i - self.optimize) or self.err_best_i==-1:
            self.pos_best_i=self.position_i.copy()
            self.err_best_i=self.err_i
        if abs(self.err_i-self.optimize)<abs(self.err_i-self.err_best_neighbor_i) or self.err_best_neighbor_i==-1:
            self.err_best_neighbor_i=self.position_i.copy()
            self.err_best_neighbor_i=self.err_i
    # update new particle velocity
    def update_velocity(self):
        w=0.7298      # constant inertia weight (how much to weigh the previous velocity)
        c1=1.49618# cognative constant
        c2=1.49618# social constant
        r1= np.random.uniform(size = (self.dims))
        r2= np.random.uniform(size = (self.dims))
        vel_cognitive=c1*r1*(self.pos_best_i-self.position_i)
        vel_social=c2*r2*(self.pos_best_neighbor_i-self.position_i)
        self.velocity_i = w*self.velocity_i + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        self.position_i=self.position_i+self.velocity_i
        np.clip(self.position_i,bounds[0],bounds[1],out = self.position_i)
        
    def update_neighbor_position(self, particle):
        if abs(self.optimize-particle.err_best_i) < abs(self.err_best_neighbor_i - self.optimize):
            self.pos_best_neighbor_i = particle.position_i.copy()
            self.err_best_neighbor_i = particle.err_best_i

