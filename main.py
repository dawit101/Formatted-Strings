#Formatted Strings

name = 'John'
age = 12

#Create the prompt, hi John. You're 12 years old.

print('hi ' + str(name) + '. You\'re ' + str(age) + ' years old.' )

print('--------------------------')

print(f'hi {name}. You\'re {age} years old.' ) #adding 'f' in the beginning creates a formatted string for python 3. This is the most preferred way for formatted strings

print('--------------------------')

print('hi {}. You\'re {} years old.'.format(name, age)) #another way to use format before python 3 was released

print('--------------------------')

print('hi {0}. You\'re {1} years old.'.format(name, age)) #similar code to line 16 but use numbers instead, 0=name and 1=age

print('--------------------------')

#More Practice
a = 'Cindy'
b = 50
print(f'hello {a}, your balance is {b}.')