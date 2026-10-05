account_balance = int(input("enter the account_balance: ")) 
requested_amount = int(input("enter the requested_amount: "))

if requested_amount <= account_balance and requested_amount % 500 == 0:
    print(f"Success! New balance: ₹{account_balance - requested_amount}")
else:
    print("Transaction denied: Invalid amount or low balance.")