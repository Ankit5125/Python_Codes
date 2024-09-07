ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

left = 0 
right = len(ls) -1

find = int(input("Enter Number You Wanted to Find : "))

while left < right :
    mid = int((left + right)/2)

    if ls[mid] == find :
        print(f"Index = {mid}")
        exit()

    elif ls[mid] > find :
        right = mid - 1
    
    else :
        left = mid + 1
    
