#!/bin/python3

#Variables And Methods
print('\n')
print('Variables and Methods')
quote = "The one who smelt it dealt it..."
print(quote)
print(quote.upper()) #upercase
print(quote.lower())#lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

relative = "father"
name = "NTP agent" #string
age = 25 #int
gpa = 4.0 #float
print(int(age))
print(int(gpa)) #only prints the number left of decimal point, does NOT round

print("My name Inigo Montoya. You killed my " + relative + ". Prepare to die.") #concatenate
print("Age this year " + str(age))
birthdays = 3
age += birthdays
print("Your age after " + str(birthdays) + " years is " + str(age))

