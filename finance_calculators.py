import math

print('''Choose either 'investment' or 'bond' from the menu below to proceed:
[Investment] - to calculate the amount of interest you'll earn interest
[Bond] - to calculate the amount you';; have to pay on a home loan.''')
selection = input(str("Investment or Bond\n")).lower()

if selection == "investment":
# 1st section: Investment selection
# if user inputs investment, the user must input the specified inputs below
    money = float(input("Enter the amount you want to invest: \n"))  # prompt user for full investing amount
    rate = float(input("Enter the interest rate (Without %). \n"))  # prompt user for interest rate at investor
    rate = (rate/100) / 12
# prompt user for how many years he wants to invest
    year = float(input("Enter the amount of years you want to invest: \n"))  
    interest = str(input("Do you want simple or compound interest? \n"))

    if interest == 'simple':
      simple_interest = money * (1 + rate * year)
      print(f"Simple interest for {year} is: {simple_interest}".format())
    elif interest:
      compound_interest = money * math.pow((1 + rate / 100),            year)  # calculate compound interest
      print(f"Compound interest for {year} years is: {compound_interest}".format())

elif selection == "bond":
# 2nd section: Bond selection
# if user selects bond, the following will happen
    prop_amount = float(input("Enter the value of the property: \n"))
    bond_interest_rate = float(input("Enter the interest rate: \n"))
    bond_interest_rate = (bond_interest_rate/100)/12
    no_of_months = float(input("Enter the number of months you plan to repay the bond: \n"))
    # formulae: x = bond_rate/12*prop_amount/1-(1+bond_rate/12)^(-repay)
    bond_payment = float(bond_interest_rate*prop_amount)/(1-(1+bond_interest_rate)**(-no_of_months))
    print(f"The monthly repayment over {no_of_months} months is: {bond_payment}".format())

else:
    print("You haven't entered a valid input. Please enter a valid input!")