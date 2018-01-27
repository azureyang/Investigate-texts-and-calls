"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
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
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""
def count():
    numbers = []

    for t in texts:
        numbers.append(t[0])
        numbers.append(t[1])
    
    for c in calls:
        numbers.append(c[0])
        numbers.append(c[1])
    
    unique_numbers = set(numbers)
    return len(unique_numbers)

print("There are {} different telephone numbers in the records.".format(count()))