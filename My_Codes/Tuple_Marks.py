length = int(input("Enter total Number of Students :"))

grade = ()

"""
print(type(grade))
for i in range(length) :
    grade += (input("Element :"),)

""" 

grade_list = []

for i in range(length):
    grade_list.append(input("Element : "))
    

grade = tuple(grade_list)
    
print(grade)    
