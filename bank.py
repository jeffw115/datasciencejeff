# Python code for ATM Bank Account
print("Welcome to Jeff's Bank!")
code = int(input("Please enter your 4-digit PIN number: ")) # Users enter 4-digit PIN number to log into bank acconut
pin = 1993 # User's 4-digit PIN number
attempts = 3 # Maximum # login attempts

# Incorrect code in first attempt
if code != pin and attempts == 3:
    # Required to allow users to re-enter code until max attempts reached
    attempts = attempts - 1
    code = int(input(f"Sorry, you have entered an incorrect PIN number. You have {attempts} more attempts. Please try again: "))

# Correct code in first attempt
if code == pin and attempts == 3:
    print("You have successfully logged into your account!")
    original_balance = 5000.50
    print(f"Your current balance is ${original_balance:.2f}") # {:.2f} displays float value with 2 decimal places
    transaction = input("Would you like to deposit or withdraw? ") # User can choose to deposit or withdraw money
    
    # If transaction is deposit
    if transaction == "deposit":
        amount = float(input("Please enter an amount: $"))
        if amount <= 0: # Amount cannot be less than or equal to $0
            print("You have entered an invalid amount.")
        else:    
            new_balance = original_balance + amount # Update new balance after deposit
            print(f"Your new balance is ${new_balance:.2f}") # User's new balance after deposit
            print("Thank you for visiting Jeff's Bank!") # Ends transaction
    
    # If transaction is withdraw
    elif transaction == "withdraw":
        amount = float(input("Please enter an amount: $"))
        if amount > original_balance: # Amount cannot exceed account balance
            print("Sorry, your current balance is less than the amount requested.")
        elif amount <= 0: # Amount cannot be less than or equal to $0
            print("You have entered an invalid amount.")
        else:
            new_balance = original_balance - amount # Update new balance after withdrawal
            print(f"Your new balance is ${new_balance:.2f}") # User's new balance after withdrawal
            print("Thank you for visiting Jeff's Bank!") # Ends transaction
    
    else:
        print("Sorry, you entered an invalid request!") # Cancels transaction

# Incorrect code in second attempt
if code != pin and attempts == 2:
    attempts = attempts - 1
    code = int(input(f"Sorry, you have entered an incorrect PIN number. You have {attempts} more attempt. Please try again: "))

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

# Incorrect code in third attempt; account is locked after 3 unsuccessful login attempts
if code != pin and attempts == 1:
    attempts = attempts + 2
    print(f"Your account has now been locked after {attempts} unsuccessful login attempts. Please try again later.")
 
# Correct code in third attempt
if code == pin and attempts == 1:
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
