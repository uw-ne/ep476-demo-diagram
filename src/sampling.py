import numpy as np

def isotropic_direction(random_pair):
   """Implement the methods to select a direction isotropically in 3-D from two random variables.

   inputs
   --------
   - random_pair: a tuple of two random variables sampled uniformly from the interval [0,1)

   outputs
   -----------
   - direction: a 1x3 numpy array with components u, v, w
   """

   w = 1 - 2 * random_pair[0]
   u = np.sqrt(1 - w * w) * np.cos(2 * np.pi * random_pair[1])
   v = np.sqrt(1 - w * w) * np.sin(2 * np.pi * random_pair[1])

   return np.array([u,v,w])

