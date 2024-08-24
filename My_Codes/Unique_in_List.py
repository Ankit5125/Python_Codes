# you are given two lists
# print the elements which are not present in list 1

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# for color in color_list_1:
#     if color in color_list_1:
#         print(color)

print(color_list_1 - color_list_2)
