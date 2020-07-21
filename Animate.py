# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:41:53 2020

@author: qtckp
"""

from Beehive import *
import numpy as np
import matplotlib.pyplot as plt


def plot1d(func = TestFunctions.Rastrigin, begin = -5, end = 5, count = 15, title = 'Rastrigin function'):
    
    def val(arr):
        return np.array([func(t) for t in arr])
    
    x = np.linspace(begin,end,150)
    y = val(x)
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.suptitle(title)
    plt.title('before start',color = 'red')
    #plt.text(-1, 35, r'before start', fontsize=14, color='red')
    plt.show()
    
    
    #bees = Bees(x[np.newaxis,:])
    bees = Bees(np.random.uniform(begin,end,(count,1)), width = 3)
    
    now = bees.x.flatten()
    best = bees.bests.flatten()
    #s1 = np.ones(count)
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.suptitle(title)
    plt.title('initialization',color = 'red')
    #plt.text(-1, 35, r'initialization', fontsize=14, color='red')
    
    plt.plot(best, val(best), 'bs', color = 'red')
    plt.plot(now, val(now), 'ro', color = 'green')
    
    plt.show()
    
    
    hive = Hive(bees,func, verbose = True)
    
    now = hive.bees.x.flatten()
    best = hive.bees.bests.flatten()
    v = hive.bees.v.flatten()
    
    #pos = float(hive.best_pos)
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.suptitle(title)
    plt.title('first step',color = 'red')
    #plt.text(-1, 35, r'first step', fontsize=14, color='red')
    
    plt.plot(best, val(best), 'bs', color = 'red')
    plt.plot(now, val(now), 'ro', color = 'green')
    
    plt.annotate('global min', xy=(float(hive.best_pos), func(hive.best_pos)), xytext=(3.5, 1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
    
    for p, v in zip(now,v):
        tmp = func(p)
        plt.arrow(p, tmp, v, 0, length_includes_head=True,
          head_width=0.8, head_length=0.2
          )
    
    
    
    plt.show()
    
    for i in range(2,8):
        
        hive.best_val, hive.best_pos = hive.bees.make_step(0.3, 2, 5, hive.best_pos, hive.best_val)
        
        now = hive.bees.x.flatten()
        best = hive.bees.bests.flatten()
        v = hive.bees.v.flatten()
        
        #pos = float(hive.best_pos)
        
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.suptitle(title)
        plt.title(f'step {i}',color = 'red')
        #plt.text(-1, 35, f'step {i}', fontsize=14, color='red')
        

        
        plt.annotate('global min', xy=(float(hive.best_pos), func(hive.best_pos)), xytext=(3.5, 1),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )
        
        for b, p in zip(best, now):
            plt.plot([b,p], val(np.array([b,p])), 'r--', color = 'blue')
            
        plt.plot(best, val(best), 'bs', color = 'red')
        plt.plot(now, val(now), 'ro', color = 'green')
        
        for p, v in zip(now,v):
            tmp = func(p)
            plt.arrow(p, tmp, v, 0, length_includes_head=True,
              head_width=0.8, head_length=0.2
              )
        plt.show()
    
    

plot1d(TestFunctions.Shvel, -65,90, count = 8, title = "Shvel")










