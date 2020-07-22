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


## Ways to get best solution



![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20with%20noise_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function_movie.gif)


![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20from%20normal%20dist.%20start%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20with%20noise%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20with%20noise%20(2d)_movie.gif)





