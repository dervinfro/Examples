import csv

file_input = input("Enter file path to input: ")

with open(file_input) as f:
	read_file = csv.reader(f)
	for x in enumerate(read_file):
		print(x[1])
		
lines = -1
for line in open(file_input):
	lines += 1
	
print("The total number of lines is: " + str(lines))
	
	