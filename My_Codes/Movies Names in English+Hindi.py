'''
this is basic program of using Dictionary in python
Dictionary is same as HashMap in java....
'''

movies = {}

n = int(input("Enter N (Names of Movies you want to Store) : "))

for i in range (n) :
    english = input("Enter English Name : ")
    hindi = input("Enter Hindi Name : ")
    # movies.update({english:hindi})
    movies[english] = hindi
    print()
    
print(movies)    
