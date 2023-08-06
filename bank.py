print("Welcome to Jeff's Bank!")
code = int(input("Please enter your 4-digit PIN number: "))
pin = 1993
attempts = 1

# Incorrect code in first attempt
if code != pin and attempts == 1:
    code = int(input("Sorry, you have entered an incorrect PIN number. You have 2 more attempts. Please try again: "))
    attempts = attempts + 1 # Required to allow users to re-enter code until max attempts

# Correct code in first attempt
if code == pin and attempts == 1:
    print("You have successfully logged into your account!")
    original_balance = 5000.50
    print(f"Your current balance is ${original_balance:.2f}") # {:.2f} displays float value with 2 decimal places
    transaction = input("Would you like to deposit or withdraw? ")
    
    # If transaction is deposit
    if transaction == "deposit":
        amount = float(input("Please enter an amount: $"))
        
        if amount <= 0:
            print("You have entered an invalid amount.")
        else:    
            new_balance = original_balance + amount
            print(f"Your new balance is ${new_balance:.2f}")
            print("Thank you for visiting Jeff's Bank!")
    
    # If transaction is withdraw
    elif transaction == "withdraw":
        amount = float(input("Please enter an amount: $"))
        
        if amount > original_balance:
            print("Sorry, your current balance is less than the amount requested.")
        elif amount <= 0:
            print("You have entered an invalid amount.")
        else:
            new_balance = original_balance - amount
            print(f"Your new balance is ${new_balance:.2f}")
            print("Thank you for visiting Jeff's Bank!")
    
    else:
        print("Sorry, you entered an invalid request!")

# Incorrext code in second attempt
if code != pin and attempts == 2:
    code = int(input("Sorry, you have entered an incorrect PIN number. You have 1 more attempt. Please try again: "))
    attempts = attempts + 1

# Correct code in second attempt
if code == pin and attempts == 2:
    print("You have successfully logged into your account!")
    original_balance = 5000.50
    print(f"Your current balance is ${original_balance:.2f}")
    transaction = input("Would you like to deposit or withdraw? ")
    
    if transaction == "deposit":
        amount = float(input("Please enter an amount: $"))
        
        if amount <= 0:
            print("You have entered an invalid amount.")
        else:    
            new_balance = original_balance + amount
            print(f"Your new balance is ${new_balance:.2f}")
            print("Thank you for visiting Jeff's Bank!")
    
    elif transaction == "withdraw":
        amount = float(input("Please enter an amount: $"))
        
        if amount > original_balance:
            print("Sorry, your current balance is less than the amount requested.")
        elif amount <= 0:
            print("You have entered an invalid amount.")
        else:
            new_balance = original_balance - amount
            print(f"Your new balance is ${new_balance:.2f}")
            print("Thank you for visiting Jeff's Bank!")
    
    else:
        print("Sorry, you entered an invalid request!")

# Incorrect code in third attempt; account is locked
if code != pin and attempts == 3:
    print("Your account has now been locked after 3 unsuccesssful attempts. Please try again later.")
 
# Correct code in third attempt
if code == pin and attempts == 3:
    print("You have successfully logged into your account!")
    original_balance = 5000.50
    print(f"Your current balance is ${original_balance:.2f}")
    transaction = input("Would you like to deposit or withdraw? ")
    
    if transaction == "deposit":
        amount = float(input("Please enter an amount: $"))
        
        if amount <= 0:
            print("You have entered an invalid amount.")
        else:    
            new_balance = original_balance + amount
            print(f"Your new balance is ${new_balance:.2f}")
            print("Thank you for visiting Jeff's Bank!")
    
    elif transaction == "withdraw":
        amount = float(input("Please enter an amount: $"))
        
        if amount > original_balance:
            print("Sorry, your current balance is less than the amount requested.")
        elif amount <= 0:
            print("You have entered an invalid amount.")
        else:
            new_balance = original_balance - amount
            print(f"Your new balance is ${new_balance:.2f}")
            print("Thank you for visiting Jeff's Bank!")