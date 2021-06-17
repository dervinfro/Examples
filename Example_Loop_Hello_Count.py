string = 'hello'
count = 1
for x in range(0,len(string)):
	print(string[0:count])
	count += 1
	if count > len(string):
		print('**end**')