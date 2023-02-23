#!/bin/python3

#Boolean Expresions and Relational Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7>5) and (5<7) #true
test_and2 = (7 < 5) and (7 > 5) #false
test_or = (7>5) or (5<7) #true
test_or2 = (7>5) or (5<7) #true

#Just look up truth table




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
