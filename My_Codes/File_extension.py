#Method 1 
string1 = "my_file.txt"
print(string1[string1.find("."):])

#Method 2
string2 = "my_file2.java"
arr = string2.split(".")
print(arr[1])
