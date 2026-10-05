order_amount=int(input("enter the order amount"))
if order_amount>=1000 or has_premium_membership:
    print("free delivery applied")
else:
    print("delivery change will apply")