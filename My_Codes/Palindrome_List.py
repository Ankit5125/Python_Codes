length = int(input("Enter Length of List :"))

my_list = []

for i in range(length):
    while True:
        try:
            my_list.append(input(f"Element {i+1} = "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

print("Your List :", my_list)

first = 0
last = len(my_list) - 1

is_palindrome = True

while first < last:
    if my_list[first] != my_list[last]:
        is_palindrome = False
        break
    first += 1
    last -= 1

if is_palindrome:
    print("True")
else:
    print("False")
