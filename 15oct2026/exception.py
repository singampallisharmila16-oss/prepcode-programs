try:
    a = input("enter number 1 : ")
    b = input("enter number 2 : ")
    print(int(a)/ int(b))
except valueError:
    print("give the numbers as a input")
except zerodivisionError:
    print("cannot divide by zero")