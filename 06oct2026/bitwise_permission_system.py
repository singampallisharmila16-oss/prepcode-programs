READ,WRITE,EXECUTE=4,2,1
perm_1 = READ|WRITE
perm_2 = READ| EXECUTE
combined = perm_1 | perm_2
print(f"combined permissions: {bin(combined)}")