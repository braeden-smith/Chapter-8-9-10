#Braeden Smith Chapter 9 Excercise 3 2/5/18

# Exercise 3
# Write a program to read through a mail log, build a histogram using a dictionary to count 
# how many messages have come from each email address, and print the dictionary.

email_sender = {}
messages = []
with open('mboxshort.txt') as f:
  for line in f:
    messages = line.split()
    if len(messages) > 3 and line.startswith('From'):
      address = messages[1]
      if address not in email_sender:
        email_sender[address] = 1
      else:
        email_sender[address] += 1
print(email_sender)