length = int(input("Enter Length of List :"))

my_list = []

for i in range(length):
    my_list.append(input("Element = "))
            
        
print("Your List :", my_list)

is_palindrom = True


"""
first = 0
last = len(my_list) - 1

while first < last:
    if my_list[first] != my_list[last]:
        is_palindrome = False
        break
    first += 1
    last -= 1

"""

rev_list = my_list.copy()
rev_list.reverse()

for i in range(len(my_list)):
    if my_list[i] != rev_list[i] :
        is_palindrom = False
        break
  
  
        
print(is_palindrom)
