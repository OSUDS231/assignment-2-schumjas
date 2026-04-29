initial_height = float(input("Please enter the initial plant height (in cm): "))
daily_growth = float(input("Please enter the daily growth as a decimal (i.e. 0.02 = 2%): "))
days = int(input("Please enter the number of days to simulate: "))
for i in range(days):
    initial_height *= (1 + daily_growth)
print(f"After {days} days, the plant is {round(initial_height,2)} cm tall.")