"""
    
    Developer: Kerem Can Belli
    Project: Python Starter Algorithms and CLI Applications
    Subproject: Password Generator
    Description: Updated English version with structured comments
    Last Review: November 2025

"""

import random

"""

    Project's character pool

    * Character pool has divided into 4 parts: big_letters, small_letters, numbers, special_characters.

"""

upper_case_letters = ["A","B","C","D","E","F","G","H","J","K","L",                          #|
                 "M","N","O","P","R","S","T","U","V","Y","Z","X","Q","W"]                   #|
lower_case_letters = ["a","b","c","d","e","f","g","h","j","k","l",                          #|  THE CHARACTER
                 "m","n","o","p","r","s","t","u","v","y","z","x","q","w"]                   #|       POOL
numbers = ["0","1","2","3","4","5","6","7","8","9"]                                         #|
special_characters = ["!","@","#","$","%","^","&","*","?"]                                  #|



print("\n--- PASSWORD GENERATOR ---")

"""

    Project's main menu:

    * Input is validated using try-except blocks to handle non-integer input.
    * It is checked whether the user requests a bank card password.

"""

while True:

    # PROJECT'S MAIN MENU STARTED

    try:
        print("\n---CHOICES---")
        users_choice_input = input("Press 1 to create bank card password\n" \
        "Press 2 to create other passwords: ")
        users_choice = int(users_choice_input) # users_choice_input is converted to integer
        if users_choice != 1 and users_choice != 2:
            print("\n--- RESULT ---")
            print("Please press just 1 or 2")
            continue
        elif users_choice == 1:                             #|
            i = 0                                           #|
            password = ""                                   #|
            while i<4:                                      #|
                password += random.choice(numbers)          #|     BANK CARD PASSWORD GENERATOR
                i += 1                                      #|
            print("\n--- RESULT ---")                       #|
            print(f"Bank card password: {password}")        #|
            break                                           #|
        else:

    # PROJECT'S MAIN MENU FINISHED

            """
                
                Choices section:

                * It is checked that the users want how long the password is.
                * The password's content which users want has been questioned
            
            """
    
    # PROJECT'S CHOICES SECTION STARTED

            while True:
                try:
                    password_length_input = input("Please input how lenght the password is: ")
                    password_length = int(password_length_input) # password_length_input is converted to integer.
                    if password_length < 8 or password_length > 18: # password_length must be less than 18 and bigger than 8. 
                        print("\n--- RESULT ---")
                        print("Please input an integer between 8 and 18")
                        continue
                    break
                except ValueError:
                    print("\n--- RESULT ---")
                    print("Please input an integer")
            while True:
                try:
                    print("\n--- CHOICES ---")     # * CHOICES MENU *
                    users_choice_input2 = input("Big and small letters must be in the password\n" \
                    "Press 1 to add numbers\n" \
                    "Press 2 to add special characters\n" \
                    "Press 3 to add both of them: ")
                    users_choice2 = int(users_choice_input2)
                    if users_choice2 != 1 and users_choice2 != 2 and users_choice2 != 3:
                        print("\n--- RESULT ---")
                        print("Please input just 1,2 or 3")
                        continue
                    break
                except ValueError:
                    print("\n--- RESULT ---")
                    print("Please input an integer.")

    # PROJECT'S CHOICES SECTION FINISHED

            """

                Password generator and output section:

                * The password's characters has been selected in line with the user's preferences.
                * The characters has been shuffled for better password.
                * The password has been created and showed.
            
            """

    # PROJECT'S PASSWORD GENERATOR AND OUTPUT SECTION STARTED

            password_list = [random.choice(upper_case_letters) , random.choice(lower_case_letters)]        #|
            remainder_length = password_length-2                                                           #|
            if users_choice2 == 1:                                                                         #|  BIG LETTERS, SMALL LETTERS
                pool_to_use = upper_case_letters + lower_case_letters + numbers                            #|  AND NUMBERS
                password_list.append(random.choice(numbers))                                               #|
                remainder_length -= 1                                                                      #|
            
            
            
            elif users_choice2 == 2:                                                                       #|
                pool_to_use = upper_case_letters + lower_case_letters + special_characters                 #|  BIG LETTERS, SMALL LETTERS
                password_list.append(random.choice(special_characters))                                    #|  AND SPECIAL CHARACTERS
                remainder_length -= 1                                                                      #|
            
            
            
            else:                                                                                          #|
                pool_to_use = upper_case_letters + lower_case_letters + numbers + special_characters       #|  ALL
                password_list.extend([random.choice(numbers), random.choice(special_characters)])          #|  CHARACTERS
                remainder_length -= 2                                                                      #|



            password_list.extend(random.choices(pool_to_use, k=remainder_length))                          #|
            random.shuffle(password_list)                                                                  #|  SHUFFLED
            real_password = "".join(password_list)                                                         #|



            print("\n--- RESULT ---")                                                                      #|
            print(f"Your password: {real_password}")                                                       #|  OUTPUT
            break                                                                                          #|

    # PROJECT'S PASSWORD GENERATOR AND OUTPUT SECTION FINISHED

    except ValueError:
        print("\n--- RESULT ---")
        print("Please input an integer.")