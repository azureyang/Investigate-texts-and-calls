"""
Intro to Python Lab 1, Task 3

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
called_by_bangalore = []
codes_prefixes = []

for c in calls:
    if c[0][:5] == '(080)' and c[1] not in called_by_bangalore:
        called_by_bangalore.append(c[1]) #get a list with unique numbers called by bangalore 

for b in called_by_bangalore:
    if b[0] =='(':
        b = b[1: b.find(')')]
        if b not in codes_prefixes:
            codes_prefixes.append(b)
    elif b[0] == '7' and b[:4] not in codes_prefixes:
        codes_prefixes.append(b[:4])
    elif b[0] == '8' and b[:4] not in codes_prefixes:
        codes_prefixes.append(b[:4])
    elif b[0] == '9' and b[:4] not in codes_prefixes:
        codes_prefixes.append(b[:4]) #get a list with only area codes and mobile prefixes

codes_prefixes = '\n'.join(sorted(codes_prefixes)) #sort the list and add line breaks
print("The numbers called by people in Bangalore have codes: \n" + codes_prefixes)


# Part B
def percent_final():
    callers = 0
    receivers = 0
    for c in calls:
        if c[0][:5] == '(080)':
            callers += 1
        if c[0][:5] == '(080)' and c[1][:5] == '(080)':
            receivers += 1
    percent = round(receivers/callers, 2) #round down to 2 decimal digits
    return str(percent)

print(percent_final() + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")