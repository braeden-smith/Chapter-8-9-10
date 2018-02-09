#Braeden Smith Chapter 9 Excercise 4 2/6/18

# Exercise 4
# After all the data has been read and the dictionary has been created, look through the 
#dictionary using a maximum loop to find who has the most messages and 
#print how many messages the person has.

largest = None
for email in email_sender:
  count = email_sender[email]
  if largest is None or count > largest :
        largest = count
        largestemail = email
print('Largest Number of Emails Sent:', largestemail, largest)