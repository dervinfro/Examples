#== is an equality check
#= is an assignment operator
mytuple = ()
print(mytuple)
print('Type: ', type(mytuple))
onetuple = (1,2,3)
print('Onetuple Second Index: ', onetuple[:3])


nesttuple = (1,2,3,(4,5,6))
print('Nest :', nesttuple)
mixedtuple = ('house', [1,2,3], 3.14)
print('Reverse Order: ', mixedtuple[::-1])
print('Index: house: ', mixedtuple.index('house'))
print('Nest Third Index: ', nesttuple[3])
print('List: ', list(nesttuple))
print('Set ', set(nesttuple))
