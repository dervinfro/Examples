from collections import OrderedDict
# Dictionary = an unordered collection of key value/pairs.
# Dictionary is mutable
# being it's unordered is why the Numerical Index (ie ref listExample.py) will not work.
# == is an equality check
# = is an assignment operator

nerd_dict = {1 : 'nerd',
			 2 : 'dork',
			 3 : 'dweeb',
			 4 : 'geek'}
#Example above: Keys are integers and values are strings

other_nerd_dict = {'nerd' : 1,
			 	   'dork' : 2,
			 	   'dweeb' : 3,
			 	   'geek' : 4}

#Keys are strings and the values are integers
nerd_dict[5] = 'loser'
nerd_dict.update({6:'chod'})
nerd_items = nerd_dict.items()
nerd_key = nerd_dict.keys()
nerd_value = nerd_dict.values()
print('Nerd Items: ',nerd_items, '\nNerd Keys: ', nerd_key, '\nNerd Value: ', nerd_value)
print(len(nerd_dict))

for x in nerd_dict:
	if x < len(nerd_dict):
		print(x, ':', nerd_dict[x], end="/ ") #see the 'end' argument, which puts output on one line
	else:
		print(x, ':', nerd_dict[x]) #see the 'end' argument is missing in this ELSE loop

for x in nerd_dict:
	print(x, ':-:', nerd_dict[x])

#example function of a dictionary items loop
def itemDictLoop():
	item_dict = {x: y for x, y in nerd_dict.items()}
	print("Dictionary Items - Looped: ", item_dict)

itemDictLoop()
