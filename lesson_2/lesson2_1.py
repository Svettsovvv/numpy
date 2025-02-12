import numpy as np

a = np.ones((3, 2))  
b = np.arange(3)
c = a + b.reshape(3, 1) 
