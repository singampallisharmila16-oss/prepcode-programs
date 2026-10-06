a=float(input("enter the frist number: "))
b=float(input("enter the second number:  "))
op=input("enter operator(+,-,*,/,%): ")
res=a+b if op == '+' else a-b if op == '-' else a*b if op == '*' else a/b if op == '/' else a%b if op== '%' else"invalid"
print("result: ",res)        