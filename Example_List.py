#== is an equality check
#= is an assignment operator
#help('scapy')
guns = ['AK','glock','m4','remington 700']
guns.insert(2,'cz')
guns.insert(1,'STI')
guns.insert(7,'Tanfoglio')
guns.append('Nighthawk')
gun_model = 'AK' in guns

x = len(guns)
current_number = 0
while current_number < x:
	length = len(str(current_number) + ' - ' + guns[current_number])
	print(str(current_number) + ' - ' + guns[current_number]+ '  Char Length: ' + str(length))
	current_number += 1
	
print('-' * 17)
#
for a, b in enumerate(guns):
	print(a,b)
	
#print('Length of guns list:', x)
print('LIST:', guns[:])
print('Bool for Model: ', gun_model)
print('POP:', guns.pop(0))
print('LIST post the pop function:', guns[:])
print('AK47' in guns)
print(guns[::-1])

if guns[3] == 'cz':
	print('AK')
else:
	print('no AK')
	

#%%
import itertools
"""
This section is a scratch pad for Leet 118 - Pascal Triangle
I am looking at ways of creating summed pair from an array and then inserting
those summed pair results into a list.
Using itertools.pairwise to sum the array and a simple assignment operator
ie array[1:1]...the reason this is [1:1] is that all the sublist matrices 
START and END with 1.  Inserting the summed pairs from the previous sublist
matrix is the solution to this problem.
"""

# Establish a multi matrix array/list
array = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Pull one of the elements out of the array and assign it to an object
array1 = array[1]


# Pull elements from the last matix of the array and insert them into array1
array1[1:1] = array[4][1:4]

# Create a FOR loop that will pairwise the array and output the sums of the pairs
sum_array= [(x+y) for (x, y) in itertools.pairwise(array1)]
