# Beehive method

Implementation of beehive method for global optimization of multidimentional functions

## Steps of algorithm

### 0 step: creating a function

Your target function should get a numpy array and return float number.

```python

f1 = lambda arr: arr[0]+arr[1]/(1+arr[0])+arr[2]*arr[3]

# convertion to numpy->float function

def target(x,y,z,q):
  return x**2+y**2*z/q

f2 = lambda arr: target(arr[0], arr[1], arr[2], arr[3])

```

The method seeks the global minimum of target function. If u want to find global maximum, use this idea:

```python

f_tmp = lambda arr: -target(arr)

#
# ... find global min
#

tagret_result = -global_min

```


### 1st step: creating bees

U should create random bees (points) on the scope of the function definition. There are several ways:

```python


from BeeHiveOptimization import Bees, Hive, BeeHive, TestFunctions, RandomPuts

import numpy as np

# 1st step is to create bees

np.random.seed(1)

# it's just numpy array with shape bees_count_x_dim

arr = np.random.uniform(low = -3, high = 5, size = (10,3))

# width parameter means the maximum range of random begging speeds

bees = Bees(arr, width = 0.2)

bees.show()

#Current bees' positions:
#[[ 0.33617604  2.76259595 -2.999085  ]
# [-0.58133942 -1.82595287 -2.26129124]
# [-1.50991831 -0.23551418  0.17413979]
# [ 1.31053387  0.35355612  2.481756  ]
# [-1.364382    4.02493949 -2.78089925]
# [ 2.36374008  0.33843842  1.46951863]
# [-1.87690449 -1.41518809  3.40595655]
# [ 4.74609261 -0.49260657  2.53858093]
# [ 4.01111322  4.15685331 -2.31964631]
# [-2.68756173 -1.64135664  4.02514003]]
#
#Current bees' speeds:
#[[-0.08033063 -0.01577847  0.09157791]
# [ 0.00663306  0.03837542 -0.03689687]
# [ 0.03730019  0.06692513 -0.09634234]
# [ 0.05002886  0.09777222  0.04963313]
# [-0.0439112   0.05785587 -0.0793548 ]
# [-0.01042129  0.0817191  -0.04127717]
# [-0.04244493 -0.07399429 -0.09612661]
# [ 0.03576711 -0.05767438 -0.04689067]
# [-0.00168537 -0.08932749  0.01482352]
# [-0.07065429  0.01786111  0.03995167]]

# u aslo can create bees by random generator like () --> random numpy array (point)

bees = Bees.get_Bees_from_randomputs(count = 10, random_gen = RandomPuts.Normal(mean = 1, std = 0.1, size = 2), width = 0.3)

bees.show()

#Current bees' positions:
#[[0.98081644 0.9112371 ]
# [0.92528417 1.16924546]
# [1.00508078 0.93630044]
# [1.01909155 1.21002551]
# [1.0120159  1.06172031]
# [1.03001703 0.96477502]
# [0.88574818 0.96506573]
# [0.97911058 1.05866232]
# [1.08389834 1.09311021]
# [1.02855873 1.08851412]]
#
#Current bees' speeds:
#[[ 0.07528273 -0.0453305 ]
# [-0.06902163  0.11876587]
# [-0.02157264  0.13945201]
# [ 0.04903245  0.03650872]
# [-0.11557621  0.13484678]
# [-0.01502636  0.02351688]
# [-0.02755896 -0.07889191]
# [ 0.12101386  0.02210385]
# [-0.1491389   0.03514347]
# [-0.05200653  0.00811743]]

```

### 2nd step: create hive and get result

```python


bees = Bees(np.random.normal(loc = 2, scale = 2, size = (100,3)), width = 3)

func = lambda arr: TestFunctions.Parabol(arr-3)

    
hive = Hive(bees, 
            func, 
            parallel = False, # use parallel evaluating of functions values for each bee? (recommented for heavy functions, f. e. integtals) 
            verbose = True) # show info about hive 

#total bees: 100
#best value (at beggining): 0.45406041997965585

# getting result

best_result, best_position = hive.get_result(max_step_count = 25, # maximun count of iteraions
                      max_fall_count = 6, # maximum count of continious iterations without better result
                      w = 0.3, fp = 2, fg = 5, # parameters of algorithm
                      latency = 1e-9, # if new_result/old_result > 1-latency then it was the iteration without better result
                      verbose = True # show the progress
                      )

#new best value = 0.22369081290807669 after 4 iteration
#new best value = 0.20481778141411794 after 5 iteration
#new best value = 0.2036698385729661 after 6 iteration
#new best value = 0.15570778532180615 after 7 iteration
#new best value = 0.06772538042802272 after 8 iteration
#new best value = 0.06060365350244633 after 9 iteration
#new best value = 0.048967304902866424 after 10 iteration
#new best value = 0.035531597911666886 after 11 iteration
#new best value = 0.018238258030885895 after 12 iteration
#new best value = 0.007999184438461721 after 13 iteration
#new best value = 0.007095161331114254 after 14 iteration
#new best value = 0.006010424290536399 after 15 iteration
#new best value = 0.0054592185233458875 after 16 iteration
#new best value = 0.003526411943370142 after 17 iteration
#new best value = 0.003212115031845861 after 18 iteration
#new best value = 0.001246361699255375 after 19 iteration
#new best value = 0.0011705559906451679 after 20 iteration
#new best value = 0.0010476941319986334 after 21 iteration
#new best value = 0.0006265651258711051 after 22 iteration
#new best value = 0.00041912821521993736 after 23 iteration
#new best value = 0.0003037094325696652 after 24 iteration
#new best value = 0.0002523002561426299 after 25 iteration



# u also can use this code (without creating a hive)

best_result, best_position = BeeHive.Minimize(func, bees, 
                 max_step_count = 100, max_fall_count = 30, 
                 w = 0.3, fp = 2, fg = 5, latency = 1e-9, 
                 verbose = False, parallel = False)


```

## Ways to get best solution



![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20with%20noise_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function_movie.gif)


![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20from%20normal%20dist.%20start%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20with%20noise%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20with%20noise%20(2d)_movie.gif)





