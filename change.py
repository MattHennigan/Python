def change(amount, coins):  
    """
    The change function will tell you how to give change in the most effecient method,
    by using the smallest number of coins possible.
    """
    
    # Find the amount of each coin that will fit in to 'amount' and pass the
    # remainder to the next line of code.
    
    if amount == 0:
        print("Please enter an amount that is more than zero.")
    if 1000 in coins:
        tens = (amount // 1000)
        amount %= 1000
    else:
        tens = 0
 
    if 500 in coins:
        fives = (amount // 500)
        amount %= 500
    else:
        fives = 0
 
    if 100 in coins:
        pounds = (amount // 100)
        amount %= 100
    else:
        pounds = 0
 
    if 50 in coins:
        fiftypennies = (amount // 50)
        amount %= 50
    else:
        fiftypennies = 0
 
    if 20 in coins:
        twentypennies = (amount // 20)
        amount %= 20
    else:
        twentypennies = 0
 
    if 10 in coins:
        tenpennies = (amount // 10)
        amount %= 10
    else:
        tenpennies = 0
 
    if 5 in coins:
        fivepennies = (amount // 5)
        amount %= 5
    else:
        fivepennies = 0
 
    if 2 in coins:
        twopennies = (amount // 2)
        amount %= 2
    else:
        twopennies = 0
 
    if 1 in coins:
        pennies = amount
        amount = 0
    else:
        pennies = 0
 
    # Check we have change by seeing if the amount is not equal to zero
    if amount != 0:
        print("Sorry. Change not available.")
        return
 
    #-------------------------------------
    # This section will print the amount of change to be given should the 
    # amount in the final check equal zero (i.e. we have correct change).
    print("Give", tens, "ten pound notes.")
    print("Give", fives, "five pound notes.")
    print("Give", pounds, "pound coins.")
    print("Give", fiftypennies, "fifty pence coins.")
    print("Give", twentypennies, "twenty pence coins.") 
    print("Give", tenpennies, "ten pence coins.")
    print("Give", fivepennies, "five pence coins.")
    print("Give", twopennies, "two pence coins.")
    print("Give", pennies, "one pence coins.")
    #-------------------------------------
 
# Testing the function for the amounts and available denominations available.
print(change(1366, [1000, 500, 100, 50, 20, 10, 5, 2, 1]))
print(change(512, [1000, 500, 100, 50, 20, 10, 5, 2, 1]))
print(change(9, [1000, 500, 100, 50, 20, 10, 5, 2, 1]))
print(change(999, [1000, 500, 100, 50, 20, 10, 5, 2, 1]))
print(change(1689, [1000, 500, 100, 50, 20, 10, 5, 2, 1]))
print(change(0, [1000, 500, 100, 50, 20, 10, 5, 2, 1]))
print(change(1689, [1000, 500, 100, 50, 10, 2, 1]))
print(change(89, [1000, 500, 100, 50, 20, 10, 5, 2]))