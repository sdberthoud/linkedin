year = 0
brutus_balance = 1.00
BRUTUS_INTEREST = 1.05
portia_balance = 100000.00
PORTIA_INTEREST = 1.04

def get_brutusBalance(currentYear):
    global year
    global brutus_balance
    global BRUTUS_INTEREST
    while year <= currentYear:
        year += 1
        brutus_balance *= BRUTUS_INTEREST
    print "At year " + str(currentYear) + ", your balance is $" + str(brutus_balance) + "."
    
def get_portiaBalance(currentYear):
    global year
    global portia_balance
    global PORTIA_INTEREST
    while year <= currentYear:
        year += 1
        portia_balance *= PORTIA_INTEREST
    print "At year " + str(currentYear) + ", your balance is $" + str(portia_balance) + "."

def find_firstYear():
    global year
    global brutus_balance
    global BRUTUS_INTEREST
    global portia_balance
    global PORTIA_INTEREST
    portia = True
    while portia == True:
        year += 1
        brutus_balance *= BRUTUS_INTEREST
        portia_balance *= PORTIA_INTEREST
        if brutus_balance > portia_balance:
            print "The first year that Brutus has more money than Portia is " + str(year)
            portia = False
        else:
            portia = True

find_firstYear()
get_brutusBalance(1204)
get_portiaBalance(1204)
        