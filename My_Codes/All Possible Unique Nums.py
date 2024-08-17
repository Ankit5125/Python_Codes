# change starting of loops according to
# numbers you want to find....

ans = []

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            
            if i != j and j != k and i != k:
                ans.append(str(i) + str(j) + str(k))

print(ans)                
