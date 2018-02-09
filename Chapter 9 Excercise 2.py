#Braeden Smith Chapter 9 Excercise 2

# Exercise 2
# Write a program that categorizes each mail message by which day of the week the 
# commit was done. To do this look for lines that start with “From”, 
# then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).

weekdays = {}
table = []
with open('mboxshort.txt') as f:
  for line in f:
    table = line.split()
    if len(table) > 3 and line.startswith('From'):
      day = table[2]
      if day not in weekdays:
        weekdays[day] = 1
      else:
        weekdays[day] += 1
print(weekdays)