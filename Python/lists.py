#!/bin/python3

#LISTS - have brackets []
nl()
print("LISTS")
movies = ["Stepbrothers", "21 Jump Street", "Shutter Island", "Marley & Me"]
print(movies[0])
print(movies[0:3]) #reuturns the first, second, and third does not inlcude place 4. 
print(len(movies))
movies.append("Jaws") #adds to end of list
print(movies)
movies.insert(2, "White Chicks")
print(movies)
movies.pop() #removes the last item

movie_list2 = ['Just Go With It', '50 First Dates', 'Happy Gilmore' ]
our_favorite_movies = movies + movie_list2
print(our_favorite_movies)

grades = [["Bob", 83], ["Alice", 90], ["Zoro", 100]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 93
print(grades)
