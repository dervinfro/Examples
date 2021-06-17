import csv

file_input = input("Enter CSV file for line count: ")

lines = 0
for line in open(file_input):
	lines += 1
	
print(lines)
	