#Braeden Smith - Chapter 8 Excercise 6
#8.6: Rewrite the program that prompts the user for a list of numbers and prints 
#out the maximum and minimum of the numbers at the end when the user enters “done.” 
#Write the program to store the numbers the user enters in a list and use the max() 
#and min() functions to compute the maximum and minimum numbers after the loop completes.

numlist = list()

print "Enter in a list of numbers and type done when you would like to quit."

while (True): 
  inp = input('Enter a number: ')
  if inp == 'done' : break
  try:
    value = int(inp)
  except:
    print 'Enter a valid number '
    quit()
  numlist.append(value) 
  
maxi = max(numlist)
mini = min(numlist)

print 'Maximum:',maxi 
print 'Minimum:',mini