initial_height = float(input("Please enter the initial plant height (in cm): "))
daily_growth = float(input("Please enter the daily growth as a decimal (i.e. 0.02 = 2%): "))
days = int(input("Please enter the number of days to simulate: "))
boost_amount = float(input("Please enter the boost amount (extra height (in cm) the plant grows every 7 days): "))
for i in range(days):
    initial_height *= (1 + daily_growth)
    if (1 + i) % 7 == 0:
        initial_height += boost_amount
print(f"After {days} days (with a {boost_amount} cm boost every 7th day), the plant is {round(initial_height,2)} cm tall.")