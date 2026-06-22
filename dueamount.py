cost = int(input("Enter the actual cost : £"))
paid = int(input("Enter how much you have paid : £"))
def calculate_change(cost, paid):
    return(paid - cost)
change = calculate_change(cost, paid)
print("You will get £ ",change,"as change")

calculate_change(paid, cost)