
# coding: utf-8

# In[15]:

get_ipython().magic(u'pylab inline')
import math

def funcion(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    y = (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)**2
    return y


# In[24]:

min_val = 0.0
max_val = 1.0
n_random = 100000

random_x1 = random.rand(n_random) * (max_val - min_val) + min_val
random_x2 = random.rand(n_random) * (max_val - min_val) + min_val
random_x3 = random.rand(n_random) * (max_val - min_val) + min_val
random_x4 = random.rand(n_random) * (max_val - min_val) + min_val
random_x5 = random.rand(n_random) * (max_val - min_val) + min_val
random_x6 = random.rand(n_random) * (max_val - min_val) + min_val
random_x7 = random.rand(n_random) * (max_val - min_val) + min_val
random_x8 = random.rand(n_random) * (max_val - min_val) + min_val
random_x9 = random.rand(n_random) * (max_val - min_val) + min_val
random_x10 = random.rand(n_random) * (max_val - min_val) + min_val

y = funcion(random_x1, random_x2, random_x3, random_x4, random_x5, random_x6, random_x7, random_x8, random_x9, random_x10)
prom = average(y)

integral = prom * (max_val - min_val)
print ("La integral es", integral)


# In[ ]:



