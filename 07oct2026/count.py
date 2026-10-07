number = 1
count = 0
while number <= 25:
    if count % 5 ==0 and count != 0:
        print()
    print(f"{number:02d}",end=" ")
    number += 1
    count += 1