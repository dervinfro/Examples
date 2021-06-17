import copy

#Set = unordered collection of unique elements
#cannot contain lists or dictionaries
#Sets can only contain immutable data
#Sets do not have a lookup ability
#== is an equality check
#= is an assignment operator
set_str = {'CZ','Glock','STI','Tanfoglio','BUL','Infinity'}
set_str2 = {'springfield','Nighthawk','STI','Limcat'}
print('Set String: ', set_str)
#Sets have no order, hence we can't call index ie set_str[1]
set_str.add('Dan Wesson')
print('Set String 2: ', set_str2)

