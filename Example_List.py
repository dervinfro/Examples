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
	
