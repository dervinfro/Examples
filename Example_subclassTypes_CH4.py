class myAge:
	age = 44
	
class myObj(myAge):
	name = 'Derek'
	age = myAge
	
x = issubclass(myObj, myAge)
print(x)
print(type(x),'\n')
y = 15
print(type(y),'\n')

z = 'HELLO'
print(type(z),'\n')
ze = z.encode()
print(type(ze))
print(hex(ze[4]))
print(z.lower())
