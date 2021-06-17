import hashlib

filepath = '/Users/user/Downloads/Python_Data/hash_text'
#METHOD ONE of how to print list--DONT USE THIS
#in_file = open('/Users/macbook/Python/hash_text','r')
##File is being read in "read" mode...NOTE if the mode was to read 'rb', the print output would be: 
##b'This will be hashed!\nThis \nwill \nbe \nhashed!'
#bf = in_file.read()
#in_file.close()
#print(bf)

##Method two of out to print list--DONT USE THIS 
#print('METHOD 2')
#with open(filepath) as fp:
#	lines = fp.readline()
##Type for lines is STR...ie print(type(lines)) = class<str>
#	count = 1
#	le = lines.encode('utf-8').strip()
#	hash.update(le)
#	hd = hash.hexdigest()
#	print('le before while: ', le)
#	while lines:
#		print('Line {}: {}, {}'.format(count, lines.strip(), hd))
#		lines = fp.readline()
#		print('le in while: ', le)
#		count += 1
#	print('\n'*2)
		


#Method three of how to print list
print('METHOD 3')
with open(filepath) as fpath:
#	print(type(fpath))
	for cnt, line in enumerate(fpath):
		hashtext = hashlib.md5(line.encode('utf-8').strip()).hexdigest()
#The above hashlib variable does NOT have the Update Method.  
#The Update Method is not needed when the running a condensed hashlib call..SEE LINE 36 ABOVE
#The strip() returns a copy of the string with both leading and trailing characters stripped.
#SEE: https://www.programiz.com/python-programming/methods/string/strip
		print('Line {}: {}: {}'.format(cnt,line.strip(),hashtext))