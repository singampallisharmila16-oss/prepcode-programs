num=int(input("enter the number: "))
starting = 2
is_prime=True
while (starting < num):
    if num % starting == 0:
        is_prime=False
    starting +=1
print(is_prime)