total_days = 1000
year =360
month = 30

no_of_years = total_days // year
remaining_days=total_days%year
no_of_months = remaining_days // month
no_of_days = remaining_days % month
print("years:",no_of_years)
print("months:",no_of_months)
print("days:",no_of_days)