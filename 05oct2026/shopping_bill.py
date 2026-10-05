notebook_price = 45
pen_price = 20

notebook_count = int(input("Enter the number of notebooks: "))
pen_count = int(input("Enter the number of pens: "))

total_notebook_price = notebook_count * notebook_price
total_pen_price = pen_count * pen_price

print(f"total is: {total_notebook_price + total_pen_price}")