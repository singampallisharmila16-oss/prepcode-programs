data=input()
data=data.split()
num1=int(data[0])
num2=int(data[1])
num3=int(data[2])
if data[0]>=data[1] and data[0]>=data[2]:
    print("data[0] is greater")
elif data[1]>=data[0] and data[1]>=data[2]:
    print("data[1] is greater")
elif data[2]>= data[0] and data[2]>=data[1]:
    print("data[2] is greater")
