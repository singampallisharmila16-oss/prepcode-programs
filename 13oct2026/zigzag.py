cases=[(4,5),(4,4)]
for num1,num2 in cases:
    for i in range(1,num1 + 1):
        if i % 2 == 1:
            for j in range(i+1,num2 + 1):
                if (i + j) % 4 == 0:
                    print(f"i = {i},j = {j}! zigzag treasure collected")
        else:
            for j in range(num2,0,-1):
                if (i + j) % 4 == 0:
                    print(f"i = {i},j = {j}! zigzag treasure collected")
    
        