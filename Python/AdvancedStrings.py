#!/bin/python3

#Advanced Strings
print("Advanced Strings")
my_name = "Agent Smith"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #delimeter

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
#escapes
quote = "She said, \"you're a player aren't you.\"" #Allows you to use quotes in the variable
print(quote)

too_much_space = "             hello moto         "
print(too_much_space)
print(too_much_space.strip())

print("A" in "Apple") #returns True
print("a" in "Apple") #returns False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #returns True!

movie3 = "The Godfather"
print("My favorite movie is {}.".format(movie3))
print("My favorite movie is %s." % movie3)
print(f"My favorite movie is {movie3}.")

