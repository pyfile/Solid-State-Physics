# The formula used for Computing is from https://en.wikipedia.org/wiki/Madelung_constant

import numpy as np
import matplotlib.pyplot as plt

def cal_in(n, e, l1, l2, l3):
	result = n * e / np.sqrt(l1**2 + l2**2 + l3**2)
	return result

def cal_surf_vertex(n, e, l1, l2, l3):
	result = n * 1/8 * e / np.sqrt(l1**2 + l2**2 + l3**2)
	return result
	
def cal_surf_face(n, e, l1, l2, l3):
	result = n * 1/2 * e / np.sqrt(l1**2 + l2**2 + l3**2)
	return result
	
def cal_surf_edge(n, e, l1, l2, l3):
	result = n * 1/4 * e / np.sqrt(l1**2 + l2**2 + l3**2)
	return result 

# a = 14.24
a = 1
n = 6
# r0 = np.sqrt(3)/4 * a

# computing K(1)'s Madelung constant, crystal:3*3*3

# crystal:1*1*1, alpha=4.7355
'''
alpha1 = cal_in(8, 1, 1/4*a, 1/4*a, 1/4*a)\
	   + cal_surf_vertex(8, -3, 1/2*a, 1/2*a, 1/2*a)\
       + cal_surf_face(6, -3, 1/2*a, 0, 0)\
       + cal_surf_edge(12, 1, 1/2*a, 1/2*a, 0)

alpha2 = cal_in(3, 1, 1/2*a, 1/2*a, 0)\
       + cal_in(3, -3, 1/2*a, 0, 0)\
       + cal_in(1, -3, 1/2*a, 1/2*a, 1/2*a)\
       + cal_in(1, 1, 1/2*a, 1/2*a, 1/2*a)\
       + cal_surf_vertex(1, 1, 1/2*a, 1/2*a, 1/2*a)\
       + cal_surf_vertex(1, 1, 3/2*a, 3/2*a, 3/2*a)\
       + cal_surf_vertex(3, 1, 1/2*a, 3/2*a, 1/2*a)\
       + cal_surf_vertex(3, 1, 3/2*a, 3/2*a, 1/2*a)\
       + cal_surf_face(3, 1, 1/2*a, 1/2*a, 1/2*a)\
       + cal_surf_face(3, 1, 3/2*a, 1/2*a, 1/2*a)\
       + cal_surf_edge(3, 1, 1/2*a, 1/2*a, 1/2*a)\
       + cal_surf_edge(6, 1, 3/2*a, 1/2*a, 1/2*a)\
       + cal_surf_edge(3, 1, 3/2*a, 3/2*a, 1/2*a)

alpha = -1 * (alpha1 + alpha2) / 2
'''

alpha1 = cal_in()
alpha = (alpha1 + alpha2) / 2
print("K(1)\'s alpha is %.4f" % alpha)
