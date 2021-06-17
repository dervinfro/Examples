import torch
import matplotlib.pyplot as plt

x = torch.randn(2,3)
y = torch.randn(5,5)

###########
## SHAPE ##
###########
'''
NOTE: x.shape[0] returns 2 (first value of x tensor).
NOTE: x.shape[1] returns 3 (second value of x tensor).
'''

print("X SHAPE[0]: \t", x.shape[0])
print("X SHAPE[1]: \t", x.shape[1:])

print(x, sep='\n')
print('')
print('Y SHAPE: \t', y.shape)
print(y, sep='\n')
print('')

################
## VIEW SHAPE ##
################
flatten_x = x.view(1, -1)  #a = x.view(x.shape[0], -1)
print("View/Shape - Flatten (X): \n", flatten_x)
print()
y_reshape = y.reshape(-1)
print("y reshape(-1): ", y_reshape, sep='\n') #this line outputs all of the fields into a SINGLE tensor
print('')
print('y reshape(-1,1):', y.reshape(-1,1), sep='\n') #this line EACH field gets IT'S OWN tensor.
print('')


#############
## FLATTEN ##
#############
#DIM 0 = ROWS
print("\nFlatten DIM 0 (X): \n", torch.flatten(x, start_dim=0))

#DIM 1 = COLUMNS
#print("\nFlatten DIM 1 (X): \t", torch.flatten(x, start_dim=1))
print()

#########################	
## ITERATE/LOOP TENSOR ##
#########################
print("Loop Tensor:")
for intr_value in range(2):
	print("Iterate Value:",intr_value, ' = ', x[intr_value], "Shape: ",x.shape[intr_value])
print()

##########	
## VIEW ##
##########

#NOTE:  Manipulate the .view line (z = x.view(-1,1)) to see how the two variable effect the x object.
#The first value of -1 is a shortcut for the total values in x, which in this case is 15 (3 * 5).
#The second value is the number of columns to be displayed.
z = x.view(-1,1)
print('View : ', z)
	
################
## TORCH TOPK ##
################

#torch.topk returns the largest element of the given input tensor.
#torch.topk(data_source, number_of_elements_to_display)
b1, b2 = torch.topk(torch.flatten(x, start_dim=0), 1)
print()
print('Top value(s) - (topk): {} || location of the top value(s) in tensor: {} '.format(b1, b2))
print()

###############
## TORCH MAX ##
###############
torch_max = torch.max(x)
print('Torch Max: ', torch_max)	
print()
# torch.max(x, dimension_number) 
# SEE: x = torch.randn(2,3)
# if num is 0, then max value returned will be along the columns
# if num is 1, then max value returned will be along the rows
torch_max_elements, torch_max_idx = torch.max(x, dim=1) 
print("Max Elements: ", torch_max_elements)
print()

# if torch.max(x, 0) then Max Index tensor will have three values, from the three columns: 
#	Max Index:  tensor([0, 0, 1])
# if torch.max(x, 1) then Max Index tensor will have two values, from the two rows:
#   Max Index:  tensor([2, 2])

print("Max Index: ", torch_max_idx)



