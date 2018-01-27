"""
Intro to Python Project 1, Task 0

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
TASK 0: 
what is the first record of texts and what is the last record of calls
Print messages: 
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
text_sender_number = texts[0][0]
text_receiver_number = texts[0][1]
text_time = texts[0][2]
print("First record of texts, {} texts {} at time {}".format(text_sender_number, text_receiver_number, text_time))

call_caller_number = calls[-1][-4]
call_receiver_number = calls[-1][-3]
call_time = calls[-1][-2]
call_duration = calls[-1][-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(call_caller_number, call_receiver_number, call_time, call_duration))