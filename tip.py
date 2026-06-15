total_menu = int(input("Enter the amount on your bill: "))
tip_perc = int(input("Enter the percentage you want to tip: "))
def total_calc(total_menu,tip_perc):
    total = total_menu*(1 + 0.01*tip_perc)
    total = round(total,2)
    print("Please pay £",total)

total_calc(total_menu,tip_perc)