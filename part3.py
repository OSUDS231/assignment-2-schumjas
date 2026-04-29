initial_height = float(input("Please enter the initial plant height (in cm): "))
daily_growth = float(input("Please enter the daily growth as a decimal (i.e. 0.02 = 2%): "))
target_height = float(input("Please enter the desired height (in cm): "))
boost_amount = float(input("Please enter the boost amount (extra height (in cm) the plant grows every 7 days): "))
days = 0
while initial_height > target_height:
    days += 1
    initial_height *= (1 + daily_growth)
    if (days) % 7 == 0:
        initial_height += boost_amount
print(f"After {days} days (with a {boost_amount} cm boost every 7th day), the plant reaches at least {round(target_height,2)} cm.")