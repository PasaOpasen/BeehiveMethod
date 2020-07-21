# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:28:36 2020

@author: qtckp
"""

import numpy as np
import random
import math
from joblib import Parallel, delayed



class RandomPuts:
    @staticmethod
    def Uniform(minimum, maximum, size):
        return lambda: np.random.uniform(minimum, maximum, size)
    @staticmethod
    def Normal(mean, std, size):
        return lambda: np.random.normal(mean, std, size)



class Bees:
    
    def __init__(self, bees, width = None):
        
        if width == None:
            #width = np.absolute(bees).max()
            width = (bees.max()-bees.min())*100/bees.shape[0]
            
        
        self.x = np.array(bees)
        self.v = (np.random.random(self.x.shape) - 0.5) * width
        self.bests = self.x.copy()
        
    @staticmethod
    def get_Bees_from_randomputs(count, random_gen, width = None):
        bees = np.array([random_gen() for _ in range(count)])
        res = Bees(bees, width)
        return res
        
        
    def set_function(self, f, parallel = False):
        self.f = f
        
        self.get_vals = (lambda: np.array(Parallel(n_jobs=-1)(delayed(f)(v) for v in self.x))) if parallel else (lambda: np.array([f(v) for v in self.x]))
        
        self.vals = self.get_vals()
        
    def make_step(self, w, fp, fg, best_pos, best_val):
        
        
        self.x += self.v
        
        
        new_vals = self.get_vals()
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
    
    def __init__(self, bees, func,  parallel = False,  verbose = True):
        
        self.bees = bees
        self.bees.set_function(func, parallel)
        
        
        
        self.best_pos = bees.bests[bees.vals.argmin(),:].flatten().copy()
        self.best_val = bees.vals.min()
        
        
        if verbose:
            print(f"total bees: {self.bees.x.shape[0]}")
            print(f"best value (at beggining): {self.best_val}")
        
    def get_result(self, max_step_count = 100, max_fall_count = 30, w = 0.3, fp = 2, fg = 5, latency = 1e-9,verbose = True):
        
        if latency != None:
            latency = 1 - latency
        
        w = 1 if math.fabs(w)>1 else math.fabs(w)
        
        count_fall = 0
        val = self.best_val
        
        for i in range(1,max_step_count+1):
            self.best_val, self.best_pos = self.bees.make_step(w, fp, fg, self.best_pos, self.best_val)
            
            if self.best_val < val:     
                
                if latency != None and self.best_val/val>latency:
                    #print(f'{self.best_val/val} > {latency}')
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
            

class BeeHive:
    pass


class TestFunctions:
    @staticmethod
    def Parabol(arr):
        return np.sum(arr**2)
    @staticmethod
    def Rastrigin(arr):
        return 10*arr.size+TestFunctions.Parabol(arr) - 10*np.sum(np.cos(2*math.pi*arr))
    @staticmethod
    def Shvel(arr):
        return -np.sum(arr*np.sin(np.sqrt(np.abs(arr))))
    


        
if __name__ == '__main__':
    
    bs = (np.random.random((200,10))-0.5)*15
    bees = Bees(bs)
    
    #bees = Bees.get_Bees_from_randomputs(200, RandomPuts.Uniform(-3,10, size = 10))
    
    #bees = Bees.get_Bees_from_randomputs(200, RandomPuts.Normal(3,2, size = 10))
    
    func = lambda arr: TestFunctions.Parabol(arr-3)
    
    hive = Hive(bees,func, parallel = False , verbose = True)
    
    res = hive.get_result(500)










