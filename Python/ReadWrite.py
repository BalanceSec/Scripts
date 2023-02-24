#!/bin/python3

months = open('months.txt')
print(months.read())#read whole file
print('\n')
#print(months.readline())#Read first line
months.close()


m2 = open('months.txt')
for month in m2:
    print(month.strip())
#months.close()
m2.close()

days = open("days.txt", "a") #a appends, w overwrites, r reads
days.write("\nTuesday")
days.close()
