num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_array1 = [1, 2, 3, 4, 5, 6, 7, 9]
num_array2 = [1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9]
main_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
num_list_missing_value = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
vowels =['a','e','i','o','u','A']
str_var = "ididntevenhavetousemyAK"
num_str = "there was 1 and 2 but not 3"

	

#######################
## FIND MISSING NUM. ##
#######################
def missing_num():
	for x in range(max(num_list_missing_value) + 1):
		if x not in num_list_missing_value:
			print('Missing Number: ', x)
		
missing_num()

######################
## MIN & MAX VALUES ##
######################

print('Min. ', min(num_array), '\tMax. ', max(num_array))

###################
## SUM TWO LISTS ##
###################

for x in num_array:
	for y in num_array1:
		if x + y == 15:
			print('Sum ', x, "+", y)
			
print('Pop 7th element from array: ', num_array1.pop(7), num_array1)


for x in range(0, len(str_var)):
	for y in range(0, len(vowels)):
		if str_var[x] == vowels[y]:
			print("match: ", str_var[x], vowels[y])


################
## PALINDROME ##
################

def palin(s):
	return s == s[::-1]
	
s = "mom"
ans = palin(s)
if ans is True:
	print('Yes - Palindrome')
else:
	print('No - Palindrome')

##################
## COUNT VOWELS ##
##################

def countVowels(my_str):
	num_vowels = 0
	for char in my_str:
		if char in "aeiouAEIOU":
			num_vowels += 1
	return num_vowels
	
cv = countVowels(str_var)
print('String: ', str_var)
print('Vowels: ', cv, '\t', 'Constants: ', len(str_var) - cv)

#############################
## Count Occurance of Char ##
#############################	

def countOccurance(my_str):
	count_occur = {}
	for x in my_str:
		if x in count_occur:
			count_occur[x] += 1
		else:
			count_occur[x] = 1
	print('Count Occurance: \n', count_occur)
	
countOccurance(str_var)
		

###################
## NUM IN STRING ##	
###################
	
def numberString(numberString):
	x = []
	for i in numberString.split():
		if i.isdigit():
			x.append(i)
	
	return x
			
print("number in str: ", numberString(num_str))

#######################
## remove duplicates ##
#######################

def rem_duplicates(x_array):
	unique = []
	for x in x_array:
		if x not in unique:
			unique.append(x)
			
	print('Unique: ', unique)

rem_duplicates(num_array2)

#############################
## show integer duplicates ##
#############################

def show_duplicates(x_array):
	duplicates = []
	for x in x_array:
		if x_array.count(x) > 1:
			duplicates.append(x)
	print('Duplicates: ', set(duplicates)) #set shows the unique duplicate values
	
show_duplicates(num_array2)

##############################
## duplicate char in string ##
##############################

def dup_char_string(string_var):
	string_dupes = []
	for x in string_var:
		if string_var.count(x) > 1:
			string_dupes.append(x)
			
	print('Duplicate CHAR in String: ', string_dupes)
	
dup_char_string(str_var)

##############################
## reverse string recursion ##
##############################

def reverse(s):
	if len(s) == 0:
		return(s)
	else:
		return reverse(s[1:]) + s[0]
	
#print(str_var)
print('Reverse recursion: ', reverse(str_var))

##########################
## count char occurence ##
##########################

def char_count(my_str,my_char):
	print('String is: ', my_str)
	print('Char is: ', my_char, 'Count is: ', my_str.count(my_char))

char_count(str_var, 'i')

##################
## binary trees ##
##################		
					

