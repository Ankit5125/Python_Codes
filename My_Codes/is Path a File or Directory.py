file = input("Enter Path : ")
file = file[::-1]
dot = '.'

for char in file:
    if char == dot:
        print("Path is a File")
        exit()

print("Path is a Directory...")