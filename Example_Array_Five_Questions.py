import random
import math

array1= [1,2,3,4,5,6,7,8,9]
array2=[1,2,3,4,5,6,7,8,9]
target = 10
la1 = len(array1) + 1
la2 = len(array2) + 1
print('Target: {}'.format(target))

def getSums(array1, array2):
	
	sums = []
	for i in range(1, la1):
		for j in range(1, la2):
			if i + j == target:
				print('Match: {} + {}'.format(i,j))
#Double for loop to take two seperate arrays and add each element of each array
			
			
getSums(array1, array2)

ran_arr = random.choice(array2)

print(ran_arr)
print(sum(array1))
print(array2.pop(ran_arr))
print(sum(array2))
					
