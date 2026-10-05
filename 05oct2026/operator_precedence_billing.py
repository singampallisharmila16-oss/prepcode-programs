food_price = int(input("enter the food_price: "))
quantity = int(input("enter the quantity: "))
discount_percentage =int(input("enter the discount_percentage: "))
delivery_charge = float(input("enter the delivery_charge: "))

# Expression following operator precedence
final_bill = (food_price * quantity) * (1 - discount_percentage / 100) + delivery_charge

# Output result
print(f"The final bill is: ${final_bill:.2f}")