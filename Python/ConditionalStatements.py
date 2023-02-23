#!/bin/python3

#Conditional Statements
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink fro you!"
print(drink(3))
print(drink(1))

def alcohol(age,money):
	if (age>= 21) and (money >=5):
		return "We getting drunk"
	elif (age >= 21) and (money < 5):
		return "Come back with more money"
	elif (age<=21) and (money > 5):
		return "Nice try kid"
	else:
		return "Get older and more money you young broke bitch"

print(alcohol(22,6))
print(alcohol(22,3))
print(alcohol(19,6))
print(alcohol(1,1))
