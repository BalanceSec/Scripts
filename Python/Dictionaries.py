#!/bin/python3

#Dictionaries - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 8} #drink is the Key, price is Value
#Key then Value
print(drinks)
employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["James", "Stan", "Marsha"]}
print(employees)
employees['Legal'] = ["Mr. NewName"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Sadie", "Oliver"]}) #adds new key:value pair
print(employees)


drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))
