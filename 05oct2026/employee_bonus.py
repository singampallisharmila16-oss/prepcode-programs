performance_rating=float(input("enter the performance_rating: "))
years_in_company=int(input("enter the years in company: "))
if performance_rating >= 4 and years_in_company >= 2:
    print("eligible for bonus")
else:
    print("not eligible for bonus")