initial_height = float(input("Please enter the initial plant height (in cm): "))
daily_growth = float(input("Please enter the daily growth as a decimal (i.e. 0.02 = 2%): "))
target_height = float(input("Please enter the desired height (in cm): "))
days = int(input("Please enter the number of days to simulate: "))
boost_amount = float(input("Please enter the height (in cm) added each time a boost is applied: "))
def noboostrun(a,b,c,d):
    for i in range(d):
        a *= (1 + b)
    return a
if noboostrun(initial_height, daily_growth, target_height, days) < target_height:
    height_dif = target_height - noboostrun(initial_height, daily_growth, target_height, days)
    boost_num = round(height_dif / boost_amount)
    boost_gap = days / boost_num
    if boost_gap >= 1:
        print(f"To reach at least {round(target_height)} cm in {days} days, apply a {boost_amount} cm boost every {round(boost_gap)} days.")
    else:
        print(f"The target height is not achievable within {days} days, even with daily boosts.")
else:
    print(f"No boosts needed! The plant will reach {round(target_height)} cm in {days} days by itself.")