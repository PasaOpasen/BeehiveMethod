# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:42:23 2021

@author: qtckp
"""

import sys
sys.path.append('..')

from BeeHiveOptimization import Bees, Hive, BeeHive

import numpy as np





bees = Bees(np.random.normal(loc = 5, scale = 2, size = (100,3000)), width = 3)

func = lambda arr: arr.sum()

    
hive = Hive(bees, 
            func, 
            parallel = False, # use parallel evaluating of functions values for each bee? (recommented for heavy functions, f. e. integtals) 
            verbose = True) # show info about hive 

#total bees: 100
#best value (at beggining): 0.45406041997965585

# getting result

best_result, best_position = hive.get_result(max_step_count = 25000, # maximun count of iteraions
                      max_fall_count = 1000, # maximum count of continious iterations without better result
                      w = 0.3, fp = 2, fg = 5, # parameters of algorithm
                      latency = 1e-9, # if new_result/old_result > 1-latency then it was the iteration without better result
                      verbose = True, # show the progress
                      max_time_seconds = 15 # max seconds of working 
                      )









