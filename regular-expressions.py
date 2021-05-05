import re


data = 'From stephen.marquard@uct.ac.az Sat Jan 5 09:14:16 2008'

# extracting a host name - using find and string slicing
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1: sppos]
print(host)

# double split pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


#regex version
y = re.findall('@([^ ]*)', data)
print(y)

#nicer regex version
y = re.findall('From .*@([^ ]*)', data)
print(y)


#escape character
x = 'We just recieved $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)