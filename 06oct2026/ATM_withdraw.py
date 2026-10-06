balance=int(input("enter the balance: "))
amount=int(input("enter the amount: "))
if amount <= balance and amount%500 == 0:
    print(" withdraw successfull") 
    balance=balance-amount
    print("remaining balance: ",balance)
else:
    print("invalid amount")