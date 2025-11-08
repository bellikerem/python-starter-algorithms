"""
    
    Developer: Kerem Can Belli
    Project: Python Starter Algorithms and CLI Applications
    Subproject: Financial Calculator
    Description: Updated English version with structured comments
    Last Review: November 2025

"""

##########################################################################

"""

    Project's main menu:

    * It is questioned what users want which option.
    * Input is validated using try-except blocks to handle non-integer input.

"""

print("\n--- FUNDAMENTAL FINANCIAL CALCULATOR ---")
while True:
    try:
        user_choice_input = input("Press 1 for basic interest calculator: \n" \
        "Press 2 for installment calculator: \n" \
        "Press 3 for VAT calculator: \n" \
        "Press 4 to quit: ") # It is questioned what users want which option.
        user_choice = int(user_choice_input) # user_choice_input is converted to integer.
        if user_choice not in [1,2,3,4]:
            print("Enter one of the numbers that you see on the screen.")
            continue
        break
    except ValueError:
        print("Please input an integer.")

##########################################################################

def check_number(prompt,type):

    """

        Validates user input to ensure it is a positive number (float or int).

        Args:
            prompt (str): The message displayed to the user.
            tip (type): The desired data type (e.g., int, float).

        Returns:
            The validated input value in the specified type.
    
    """

    while True:
        try:
            value = type(input(prompt))
            if value<=0:
                print("Please input a positive rational number.") # Rational number is checked whether it is positive or not.
                continue
            return value
        except ValueError:
            print("Please input a rational number.")

##########################################################################

def basic_interest_calculator():

    """

        basic_interest_calculator function:

        * Base money, interest rate and time values are wanted from users in this function.
        * Interest difference and final amount are calculated and printed.
    
    """

    print("\n--- BASIC INTEREST CALCULATOR ---")
    # Base money, interest rate and time values are wanted from users in this function.
    base_money = check_number("Enter your base money amount (TL): ", int)
    interest_rate = check_number("Enter your annual interest rate (%): ", float)
    time = check_number("Enter time (month): ", int)

    # Interest difference and final amount are calculated and printed.
    interest_difference = base_money * (interest_rate/100) * (time/12)
    final_amount = interest_difference + base_money

    print("\n--- RESULT ---")
    print(f"Interest difference: {interest_difference} TL")
    print(f"Total amount: {final_amount} TL")

##########################################################################

def installment_calculator():

    """

        installment_calculator function:

        * Credit amount, interest rate and time are wanted from users in this function
        * User's monthly credit installment is calculated with using special formula and showed the users.
    
    """

    print("\n--- INSTALLMENT CALCULATOR ---")

    # Credit amount, interest rate and time are wanted from users in this function
    credit_amount = check_number("Enter your credit amount: ", int)
    interest_rate = check_number("Enter your annual interest rate (%): ", float)
    time = check_number("Enter time (month): ", int)

    # User's monthly credit installment is calculated with using special formula and showed the users.
    interest_rate = interest_rate/(100*12)
    formula_top_section = interest_rate*((1 + interest_rate)**time)
    formula_bottom_section = ((1 + interest_rate)**time) - 1
    formula = formula_top_section/formula_bottom_section
    monthly_installment = credit_amount * formula

    print("\n--- RESULT ---")
    print(f"Your monthly credit installment: {monthly_installment} TL")

##########################################################################

def vat_calculator():

    """

        vat_calculator function:

        * Total amount and vat values are wanted from users
        * It is questioned that users want to remove vat value from total amount or add.
        * Input is validated using try-except blocks to handle non-integer input.
        * The result is displayed based on the user's preference. 
    
    """

    print("\n--- VAT CALCULATOR ---")

    # Total amount and vat values are wanted from users
    total_amount = check_number("Enter the total amount: ", int)
    vat = check_number("Enter your vat rate (%): ", int)
    while True:
        try:
            decision_input = input("Press 1 to add VAT\n"
            "Press 2 to remove VAT: ") # It is questioned that users want to remove vat value from total amount or add.
            decision = int(decision_input)
            if decision not in [1,2]:
                print("Please enter 1 or 2.") # Input is validated using try-except blocks to handle non-integer input.
                continue
            break
        except ValueError:
            print("Please input an integer.")
    if decision == 1:
        vat_amount = total_amount * (vat/100)
        added_amount = total_amount + vat_amount

        print("\n--- RESULT ---")
        # The result is displayed based on the user's preference.
        print(f"Price with VAT added: {added_amount} TL")
    else:
        vat_amount = total_amount * (vat/100)
        removed_amount = total_amount - vat_amount

        print("\n--- RESULT ---")
        # The result is displayed based on the user's preference.
        print(f"Price with VAT removed: {removed_amount} TL")

##########################################################################

if user_choice == 1:
    basic_interest_calculator()
elif user_choice == 2:
    installment_calculator()
elif user_choice == 3:
    vat_calculator()
else:
    exit()