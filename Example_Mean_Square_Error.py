import numpy as np
from sklearn.metrics import mean_squared_error


x = np.arange(1,476)
y = np.arange(0.25,5.0,0.01)

print('Len of x: {} and len of y: {}'.format(len(x), len(y)))

# MSE using the sklearn.metrics module
print('MSE (sklearn): ', mean_squared_error(y,x))

# Long hand version of the MSE using np.square
print('MSE (np.square): ', np.square(np.subtract(y,x)).mean())

# Long hand version of the MSE without using sklearn or np
print('MSE (Long Hand): ', ((x-y)**2).mean())

# Long hand version of the MSE without using sklearn or np
print('MSE (Long Hand): ', ((y-x)**2).mean())

# Long hand version of the MSE without using mean
print('MSE (Long Hand): ', sum((x-y)**2)/len(x))


print(np.subtract(x,y).mean())
print(np.subtract(y,x).mean())
