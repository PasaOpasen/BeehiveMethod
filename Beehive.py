# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:28:36 2020

@author: qtckp
"""

import numpy as np
import random
import math



class Bees:
    
    def __init__(self, bees, width = None):
        
        if width == None:
            width = np.absolute(bees).max()
        
        self.x = np.array(bees)
        self.v = (np.random.random(self.x.shape) - 0.5) * width
        self.bests = self.x.copy()
        
    def set_function(self, f):
        self.f = f
        self.vals = np.array([f(v) for v in self.x])
        
    def make_step(self, w, fp, fg, best_pos, best_val):
        
        
        self.x += self.v
        
        
        new_vals = np.array([self.f(v) for v in self.x])
        inds = new_vals < self.vals
        self.bests[inds,:] = self.x[inds,:].copy()
        
        minimum = new_vals.min()
        if minimum < best_val:
            best_val = minimum
            best_pos = self.bests[new_vals.argmin(),:].flatten().copy()
            #print(best_pos)
        self.vals[inds] = new_vals[inds]
        
        
        
        fi = fg + fp
        coef = 2*w/math.fabs(2-fi-math.sqrt(fi*(fi-4)))
        
        self.v = coef * (self.v + 
                         fp * np.random.random(self.x.shape)*(self.bests - self.x) + 
                         fg * np.random.random(self.x.shape)*(best_pos - self.x) )
        
        return best_val, best_pos
        



class Hive:
    
    def __init__(self, bees, func,  verbose = True):
        
        self.bees = bees
        self.bees.set_function(func)
        
        
        
        self.best_pos = bees.bests[bees.vals.argmin(),:].flatten().copy()
        self.best_val = bees.vals.min()
        
        
        if verbose:
            print(f"total bees: {self.bees.x.shape[0]}")
            print(f"best value: {self.best_val}")
        
    def get_result(self, max_step_count = 100, max_fall_count = 50, w = 0.3, fp = 2, fg = 5, max_new_percent = 99.99999, verbose = True):
        
        
        if max_new_percent != None:
            max_new_percent = max_new_percent/100
        
        count_fall = 0
        val = self.best_val
        
        for i in range(1,max_step_count+1):
            self.best_val, self.best_pos = self.bees.make_step(w, fp, fg, self.best_pos, self.best_val)
            
            if self.best_val < val:     
                
                if max_new_percent != None and self.best_val/val>max_new_percent:
                    #if verbose:
                    #    print(f'I should stop if new_val/old_val > {max_new_percent} (now {self.best_val/val})')
                    #return self.best_val, self.best_pos
                    count_fall+=1
                
                if verbose:
                    print(f'new best value = {self.best_val} after {i} iteration')
                    val = self.best_val
                
                
                
            else:
                
                count_fall+=1
                
            if count_fall == max_fall_count:
                    
                if verbose:
                    print(f'I should stop after {count_fall} fallen iterations')
                    
                return self.best_val, self.best_pos
        
        return self.best_val, self.best_pos
            
            
        
if __name__ == '__main__':
    
    bs = (np.random.random((200,10))-0.5)*15
    bees = Bees(bs)
    
    func = lambda arr: np.sum( (arr-3)**2)
    
    hive = Hive(bees,func, True)
    
    res = hive.get_result(500)










