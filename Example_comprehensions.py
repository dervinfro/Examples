num = range(10)
print('Range 1-10 squared: ', [x * x for x in num])
#LIST COMPREHENSION: The above is a condensed version of a for loop.  The above for loop is in 'list' brackets []
print('*' * 18)
print('Divisable by two (2): ', [x * x for x in num if x % 2 == 0])
print('*' * 18)
letters = [letter.upper() for letter in 'worldwide']
print(letters)
ltos = ' '.join(map(str, letters))
print(ltos)
print('*' * 18)
print('Multiples of 27: ', [i for i in range(0, 300) if i % 27 == 0])
print('*' * 18)
print('Math: ',[i for i in "MATHEMATICS" if i in ['A','E','I','O','U']])
