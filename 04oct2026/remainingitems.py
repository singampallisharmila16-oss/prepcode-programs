number_of_items=int(input("enter the product count"))
products_count_per_box=int(input("enter the box size/box:"))

total_box_needed=number_of_items // products_count_per_box
remaining_items=number_of_items % products_count_per_box

print(f"total boxes needed {total_box_needed} and remaining items: {remaining_items}")