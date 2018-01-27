"""
Intro to Python Lab 1, Task 2

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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""
caller_time = {}
receiver_time = {}

for c in calls:
    k1 = c[0]
    if k1 not in caller_time:
        caller_time[k1] = int(c[3])
    else:
        caller_time[k1] += int(c[3]) #get a dict with unique caller numbers and time

    k2 = c[1]
    if k2 not in receiver_time:
        receiver_time[k2] = int(c[3])
    else:
        receiver_time[k2] += int(c[3]) #get a dict with unique receiver numbers and time

for k, v in receiver_time.items():
    if k in caller_time.keys():
        caller_time[k] += v
    else:
        caller_time[k] = v #merge receiver_time into caller_time

total_time = max(caller_time.values())
for k, v in caller_time.items():
    if caller_time[k] == total_time:
        telephone_number = k #find the maximum value and its key

print ("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone_number, total_time))