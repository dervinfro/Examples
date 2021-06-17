word = 'python'

we = word.encode()

python_list = []

for i in range(0, len(word)):
	python_list.append(hex(we[i]))
	print(hex(we[i]))
	i+=1

print(list(word))
print(python_list)	

text = 'mymanfromamsterdam'

word_list = []

for i in range(0, len(text)):
	word_list.append(text[i])
	i+=1

print(word_list[0:len(word_list)]) #same as print(word_list)

#.split creates two indexes [0] & [1]
#The [1] is all of the indexed contents after 'man' AKA fromamsterdam
#Change that to [0], and it would print 'my'
string_split = text.split('man')[1] 
print('String Split: {}'.format(string_split))
