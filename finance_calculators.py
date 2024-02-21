import math

# Selection of inputs for whether they want an investment or a bond

user_selection = "\ninvestment - to calculate the amount of interest you'll earn on your investment\n"
user_selection += "bond - to calculate the amount you'll have to pay on a home loan\n"
user_selection += "\nEnter either 'investment' or 'bond' from the menu above to proceed:"

selection = input(user_selection)
selection = selection.lower()
selection = selection.strip()

# If condition regarding if they choose investment what they want to deposit,what their interest rate is and the years they would like to invest.
#Data types connected to defined variable for later calculations in the code.


if (selection == "investment"):

    money_deposit = float(input("\nHow much money are you depositing:"))
    interest = float(input("Enter your interest rate:"))
    amount_years = int(input("How many years do you plan on investing?:"))

    simple_interest = money_deposit * (1 + interest/100 * amount_years)
    compound_interest = money_deposit * math.pow ((1+(interest/100)),amount_years)

# Input asking whether they would like simple or compound interest and in regards to their response what their investment will equate to.

    interest = (input("\nWould you like simple or compound interest on your investment?:")).lower()

    if interest == "simple":
        print("\nYou have selected simple interest")
        print(f"\nInvestment return after {amount_years} years will be: {simple_interest:.2f}")

    elif interest == "compound":
        print("\nYou have selected compound interest")
        print(f"\nYour investment return after {amount_years} years will be {compound_interest:.2f}")
    else:
        print("Error, you have chosen an invalid interest option")

# Otherwise if their investment is a bond, values on their house, interest rate and time they expect to pay back the bond are requested.  
# Variables for mathematical equations of values are defined in terms of bond repayment.    

elif (selection == "bond"):

    house_value=float(input("\nWhat is the present value of the house?"))
    interest_rate=float(input("What is the interest rate?"))
    months=int(input("How many months do you intend to take to repay the bond?"))

    interest_rate = (interest_rate / 100) / 12
    bond_repayment = (interest_rate * house_value) / (1-(1 + interest_rate) ** (-months))


    print(f"\nYour monthly repayments will be:{bond_repayment:.2f}")

# If input is in none of these categories they have put in the wrong input

else:
    print("Error you have entered and invalid response")
    


