number = 20

while number < 25:
	print(number)
	number += 1
##	
#name = 'Derek'
#print(name)
#print(type(name))
#while name == 'Derek':
#	print('That is the name')
##	break
#	name ='rowan'
#	print(name)
	
#num = 0 
#
#while num in range(0,10):
#	if num % 2 == 0:
#		print('even number: {}'.format(num))
#	num += 1
#	
#vi = int(input('enter a integer: '))
#length = 0
#while vi > 0:
#	vi //= 10
#	length += 1
#print('number of digits: {}'.format(length))

#x,y = 0,8
#while(x<y): x += 1; print(x)
##This is where the semi-colon is used in Python, to seperate commands on a single line.
#	
#x = 1
#
#while x < 5:
#	y = 1
#	while y < 5:
#		print(x,y)
#		y += 1
#	x += 1
	
#nl = [10,20,30,40,50]
#count = 0
#while count < len(nl):
#	print(nl[count])
#	count += 1
	
#while count	< len(nl):
#	print(count)
#	count += 1
	
#total = 0
#element = 0

#while element < len(nl):
#	total = total + nl[element]
#	print(total)
#	element += 1
#print('total count of all of the elements: {}'.format(element))

#for element in nl:
#	total += element
#	print(total)
#print('total count of all of the elements: {}'.format(len(nl)))
#print('*' * 18)
#el = []
#ol = []
#num = 0
#
#
#while num < 50:
#	if num % 2 == 0:
#		el.append(num)
#	else:
#		ol.append(num)
#	num += 1
#print('even: {}'.format(el))
#print('odd: {}'.format(ol))
#print('*' * 18)
#
#cd = [-20, -10, 0, 10, 20, 30, 70]
#index = 0
#print('   C     F')
#while index < len(cd):
#	C = cd[index]
#	F = (9.0/5)*C + 32
#	print('   {}   {}'.format(C,F))
#	index += 1
#print('*' * 18)
#
#nl = ['john','jay','rambo']
#al = [22,33,44]
#index = 0
#while index < len(nl):
#	print(nl[index], ' is ', al[index])
#	index += 1
#print('*' * 18)
#
#char_name = ('john','jay','rambo')
#long_name = char_name[2]
#index = 0
#while index < len(char_name):
#	if len(long_name) < len(char_name[index]):
#		long_name = char_name[index]
#	index += 1
#print('Long name is: {}'.format(long_name))
#print('*' * 18)

#num = 10
#
#while num in range(10,100):
#	print(num)
#	if num == 50:
#		break
#	num += 10
#print('out of loop')
#print('*' * 18)

#num_value = 10
#while num_value > 0:
#	print('current value {}'.format(num_value))
#	if num_value == 5:
#		pass
#		print('this is the pass block')
#	num_value = num_value - 1
#print('end block')

##The following For statement is a comparison to the While statement above
##The For statement skips over the printing of the number 5 in this range.
##This is due to the fact that "print" is outside of the "if" loop and in the "else" statment
##The above "while" statment has the print PRIOR to the if num_value == 5.
#for num_value in range(0,10):
#	if num_value == 5:
#		pass
#		print('this is the pass block')
#	else:
#		print('current value: {}'.format(num_value))
#
#	num_value -= 1
#print('end block')
#print('*' * 18)
#
#num = 0 
#while num < 10:
#	num += 1
#	if num % 2 == 0:
#		continue
##The continue statement continues the loop iteration (AKA it does not move onto the print statement) for all even numbers.
#	print('Odd number: {}'.format(num))
#print('end while-continue')
#print('*' * 18)
#ml = []
#num = 0
#while num < 50:
#	num += 1
#	if num % 5 == 0 or num % 7 == 0:
#		continue
#	ml.append(num)
#	
#print(ml)
#print('*' * 18)
#while True:
#	value = input('\nEnter a number: ')
#	if value == 'out':
#		print('Program Exit')
#		break
#	if not value.isdigit():
#		print('numbers only')
#		continue
#	value = int(value)
#	print('Cube of {} is {}'.format(value, value ** 3))

	
	