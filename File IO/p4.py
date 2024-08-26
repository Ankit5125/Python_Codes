file = open("F4.txt" , "a")

n = int(input("lines you want to add : "))

for i in range(n):
    file.write(input(f"Enter line {i+1} : "))
    file.write("\n")

file.write("\n")

print("Text Added Successfully...")

file.close()