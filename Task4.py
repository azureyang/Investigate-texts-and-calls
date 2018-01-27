"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

numbers_regular = []
numbers_called = []
for t in texts:
    numbers_regular.append(t[0])
    numbers_regular.append(t[1])    
for c in calls:
    numbers_regular.append(c[1]) #get a list of all regular numbers
    numbers_called.append(c[0]) #get a list of numbers that have outgoing call records 
    
telemarketers = set(numbers_called) - set(numbers_regular) #remove dupilcates and find items only in numbers_called
telemarketers_list = '\n'.join(sorted(list(telemarketers))) #sort and add breaks

print("These numbers could be telemarketers: \n" + telemarketers_list)