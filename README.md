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


### 1st: creating bees

U should create random bees (points) on the scope of the function definition.





![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20with%20noise_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function_movie.gif)


![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20from%20normal%20dist.%20start%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Rastrigin%20function%20with%20noise%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20(2d)_movie.gif)

![1](https://github.com/PasaOpasen/BeehiveMethod/blob/master/images/Shvel%20function%20with%20noise%20(2d)_movie.gif)





