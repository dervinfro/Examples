import numpy as np

a = [[3,2],[4,6]]
b = [[5,3],[200,100]]

'''
NOTE:
	(3 a[1:1]* 5 b[1:1]) + (2 a[1:2] * 200) = 415
	(4 a[2:1] * 5 b[1:1]) + (6 a[2:2] * 200) = 1220
	(3 a[1:1]* 3 b[1:2]) + (2 2 a[1:2] * 100 b[2:2]) = 209
	(4 a[2:1]* 3 b[1:2]) + (6 a[2:2] * 100 b[2:2]) = 612
	
'''

print(np.matmul(a,b))
print(np.dot(a,b))
'''
NOTE: See tutorial on np.dot (https://www.tutorialspoint.com/numpy/numpy_dot.htm)
np.dot is the same output as np.matmul....at least when it comes to 2 X 2 matrices.  As of 21JUN, I have not test on anything more that 2 X 2 matrices.
'''
