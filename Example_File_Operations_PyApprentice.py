#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 23:00:24 2021

@author: user
"""

# =============================================================================
# Opening a File in Python
# =============================================================================

# Run a shell command (!) within the IDE to output results to Terminal
!cat ./Track_2_Python_Apprentice/sources/sample.txt #noqa

# Open the file and see file object details in Terminal
open("./Track_2_Python_Apprentice/sources/sample.txt")

# Open the file to the file object
file = open("./Track_2_Python_Apprentice/sources/sample.txt")

# File mode is read "r"
file.mode

# File name and location
file.name

# Returns a boolean value
file.closed

# Close the file with the .close() method
file.close()

# Reopen the file
file = open("./Track_2_Python_Apprentice/sources/sample.txt")

# Read the file
file.read()

# Bring file cursor to initial position
file.seek(0)

# Read the first four from the .seek() position
file.read(5)

# Get the current file position
file.tell()

file.read(5)

# =============================================================================
# The Different Read Functions
# =============================================================================

file.seek(0)

file.read(5)

# Reads line from cursor position to end of line
file.readline()

# Reset cursor to beginning
file.seek(0)

# Read lines
file.readlines()

# Returns a boolean value (False = file open // True = file closed)
file.closed

# Close file
file.close()

#%%
with open("./Track_2_Python_Apprentice/sources/sample.txt") as f:
	line = f.readlines()

	while line:
		print(line)
		line = f.readline()
		
#%%
# =============================================================================
# Writing to Files in Python
# =============================================================================

file = open("./Track_2_Python_Apprentice/sources/example.txt", 'w')

file.close()

!cat ./Track_2_Python_Apprentice/sources/example.txt

file.closed

file = open("./Track_2_Python_Apprentice/sources/example.txt", 'w')

file.write("This is a test write operation")

file.seek(6)

file.write("examine")

file.close()

!cat ./Track_2_Python_Apprentice/sources/example.txt

#%%%

file_write = open("./Track_2_Python_Apprentice/sources/example.txt")

for lines in file_write:
	print(lines)

#%%%
with open("./Track_2_Python_Apprentice/sources/example.txt", "w") as f:
	f.write("First Line\n")
	f.write("Second Line\n")
	f.write("Third Line \n")
	
!cat ./Track_2_Python_Apprentice/sources/example.txt

#%%%
# Open the file to append its contents
file = open("./Track_2_Python_Apprentice/sources/example.txt", "a")

file.tell()

#%%%
file.writelines(["This is the fourth line appended \n",
				 "This is the fifth line appended \n", 
				 "This is the sixth line appended \n"])

file = open("./Track_2_Python_Apprentice/sources/example.txt", "r")

file.readlines()

file.fileno()

# This function returns a boolean if file stream is interactive
file.isatty()

file.readable()

file.writable()

file.close()

#%%
# =============================================================================
# The r+ and a+ modes
# =============================================================================

f = open("./Track_2_Python_Apprentice/sources/sample.txt", "a")

# Tells the last integer position of the cursor
f.tell()

# Use os.stat to confirm output of f.tell()
import os
os.stat("./Track_2_Python_Apprentice/sources/sample.txt").st_size

# Truncate the file size to the value passed.
f.truncate(37)

f.close()

f = open("./Track_2_Python_Apprentice/sources/sample.txt","r")

f.read()

!cat ./Track_2_Python_Apprentice/sources/example.txt

# Open the example file in r+ (+ means we can read & write)
# Cursor starts at the beginning of the file AND overwrites content
f = open("./Track_2_Python_Apprentice/sources/example.txt","r+")
f.writelines("We are doing and 'r' operation")
f.close()

!cat ./Track_2_Python_Apprentice/sources/example.txt

# Open the example file in a+ (+ means we can append)
# Cursor starts at the end of the file
f = open("./Track_2_Python_Apprentice/sources/example.txt","a+")
f.writelines("We are writing an 'a+' example.")
f.close()

!cat ./Track_2_Python_Apprentice/sources/example.txt

# Rename a file name
os.rename("./Track_2_Python_Apprentice/sources/example.txt","./Track_2_Python_Apprentice/sources/changed_example.txt")

!cat ./Track_2_Python_Apprentice/sources/changed_example.txt

# Delete a file
os.remove("./Track_2_Python_Apprentice/sources/changed_example.txt")

!cat ./Track_2_Python_Apprentice/sources/changed_example.txt

#%%
# =============================================================================
# Reading JSON in Python
# =============================================================================

!cat /Users/user/Downloads/Python_Data/Track_2_Python_Apprentice/sources_5/currency.json

import json

#%%%
car = """{ "model":"Civic", 
"make":"Honda", 
"variants": ["Sedan","Coupe"]}"""
	
# Loads the car object into type dict (dictionary)
# Takes string (car) and returns a dictionary (car_dict) using json.loads
# **Take note of the "s" in json.loads...different from below in the open**
car_dict = json.loads(car)

# Confirm dict type
type(car_dict)

# Pull down a single field from the JSON
car_dict['model']

!cat /Users/user/Downloads/Python_Data/Track_2_Python_Apprentice/sources_5/currency.json

#%%%
# Open the JSON file and return a dictionary
with open("./Track_2_Python_Apprentice/sources_5/currency.json") as json_file:
	data = json.load(json_file)
	print(data)
	
# Define currency dictionary
currency = { "Country": "India", "Currency": "Rupee"  }

# Dumps writes dictionary to JSON string
json_var = json.dumps(currency)

json_var

type(json_var)

#%%%
with open("./Track_2_Python_Apprentice/sources_5/currency.json","w") as json_file:
	json_file.write(json_var)
	
!cat ./Track_2_Python_Apprentice/sources_5/currency.json

#%%
# =============================================================================
# Transform Python Objects into JSON
# =============================================================================

dessert = {"Name": "Ice cream",
           "Flavours": ["Chocolate", "Pineapple"],
           "Toppings": True,
           "WaffleCone": "Yes"
}

# json.dumps writes dictionary into JSON string
dessert_str = json.dumps(dessert)

dessert_str

type(dessert_str)

#%%
# Save the contents of a json string to a file using with open
with open("./Track_2_Python_Apprentice/sources_5/eat.txt","w") as json_file:
	json.dump(dessert, json_file)
	
# Use cat to confirm contents of text file
!cat ./Track_2_Python_Apprentice/sources_5/eat.txt

dessert

json.dumps(dessert, indent=2)

# Change separators between key & value
json.dumps(dessert, separators=(":","="))

# Another example using different separators
json.dumps(dessert, separators=("|","="))

# Keys sorted
json.dumps(dessert, sort_keys=True)

# Keys are ordered in the manner they were defined.
json.dumps(dessert, sort_keys=False)

#%%
# =============================================================================
# Parsing Diff Forms of CSV files
# =============================================================================

import csv

!cat ./Track_2_Python_Apprentice/sources_6/record.csv

!cat ./Track_2_Python_Apprentice/sources_6/record_pipe.csv

!cat ./Track_2_Python_Apprentice/sources_6/record_tab.csv

#%%%
# Open record.csv -> read the file -> FOR loop and print
# NOTE: Each row has multiple strings because the default demlimiter is a comma.
file = open("./Track_2_Python_Apprentice/sources_6/record.csv","r")

with file:
	read = csv.reader(file)
	
	for row in read:
		print(row)
#%%%		
# Open record_pipe.csv -> read the file -> FOR loop and print
# NOTE: each row is a single sting because we have not told it how to delimit with the pipe character
file = open("./Track_2_Python_Apprentice/sources_6/record_pipe.csv","r")

with file:
	read = csv.reader(file)
	
	for row in read:
		print(row)
		
#%%%		
# Open record_pipe.csv -> read the file -> FOR loop and print
# NOTE: each row is NOW delimited with the .reader attribute of delimiter set to pipe ("|")
file = open("./Track_2_Python_Apprentice/sources_6/record_pipe.csv","r")

with file:
	read = csv.reader(file, delimiter="|")
	
	for row in read:
		print(row)
		
#%%%
# Open record_pipe.csv -> read the file -> FOR loop and print
# NOTE: each row is NOW delimited with the .reader attribute of delimiter set to tab ("\t")
file = open("./Track_2_Python_Apprentice/sources_6/record_tab.csv","r")

with file:
	read = csv.reader(file, delimiter="\t")
	
	for row in read:
		print(row)
		
		
#%%
# =============================================================================
# Transform Python Objects into CSV
# =============================================================================

file = open("./Track_2_Python_Apprentice/sources_6/record.csv","r")

with file:
	reader = csv.DictReader(file)
	
	for row in reader:
		print(dict(row))

#%%%
names = [['FirstName', 'LastName'], 
         ['Sofia', 'Reyes'], 
         ['Jerome', 'Jackson'], 
         ['Jia', 'Zhong']]

#%%%
file = open("./Track_2_Python_Apprentice/sources_6/names.csv","w")

with file:
	file_writer = csv.writer(file)
	for row in names:
		file_writer.writerow(row)
		
!cat ./Track_2_Python_Apprentice/sources_6/names.csv

#%%%
nums = [[10,20,30],
       [40,50,60],
       [70,80,90]]

file = open("./Track_2_Python_Apprentice/sources_6/number.csv","w")

with file:
	write = csv.writer(file)
	write.writerows(nums)
	
!cat ./Track_2_Python_Apprentice/sources_6/number.csv

#%%%
file = open('./Track_2_Python_Apprentice/sources_6/names.csv', 'w')

with file:
    
    fnames = ['FirstName', 'LastName']
    writer = csv.DictWriter(file, fieldnames=fnames)    

    writer.writeheader()
    writer.writerow({'FirstName' : 'Sofia', 'LastName': 'Reyes'})
    writer.writerow({'FirstName' : 'Jerome', 'LastName': 'Jackson'})
    writer.writerow({'FirstName' : 'Jia', 'LastName': 'Zhong'})
	
!cat ./Track_2_Python_Apprentice/sources_6/names.csv

#%%
# =============================================================================
# CSV Dialects
# =============================================================================

# NOTE: research this if you ever want to build out custom delimiters
csv.register_dialect

















