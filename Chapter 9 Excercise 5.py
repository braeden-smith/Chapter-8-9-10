#Braeden Smith Chapter 9 Excercise 5 2/7/18

# Ex. 5 This program records the domain name (instead of the address) where the 
# message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

#My idea for splitting strings was guided by 
#http://stackoverflow.com/questions/1633932/slice-a-string-after-a-certain-phrase
#and http://stackoverflow.com/questions/4945548/remove-the-first-character-of-a-string
domain_name = {}
domain_table = []
with open('mboxshort.txt') as f:
  for line in f:
    domain_table = line.split()
    if len(domain_table) > 3 and line.startswith('From'):
      email_address = domain_table[1]
      section_1 = (email_address[email_address.find("@"):])
      section_2 = section_1[1:]
      if section_2 not in domain_name:
        domain_name[section_2] = 1
      else:
        domain_name[section_2] += 1
print(domain_name)