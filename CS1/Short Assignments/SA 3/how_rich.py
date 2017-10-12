year = 0
brutus_balance = 1.00
BRUTUS_INTEREST = 1.05

def get_balance(currentYear):
    global year
    global brutus_balance
    global BRUTUS_INTEREST
    while year <= currentYear:
        year += 1
        brutus_balance *= BRUTUS_INTEREST
    print "At year " + str(currentYear) + ", your balance is $" + str(brutus_balance) + "."
    
get_balance(2014)