#User Pin and Balance
current_pin = "1234"
balance = 50000.0

print("Welcome to the ATM!")

#User input
input_pin = input("Please enter your 4 digit pin: ")

#Pin verification
if input_pin != current_pin:
    print("Incorrect PIN. Access Blocked.")
else:
    print("=" * 30)
    print("     Main Menu     ")
    print("=" * 30)
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Change Pin")
    print("5. Exit")
    print("-" * 30)

    choice = input("Please select an option (1-5): ").strip()
    print("-" * 30)

    #option 1
    if choice == "1":
        print("Your current balance is", balance)

    #option 2
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient Funds")
        else:
            balance -= amount
            print("You have withdrawn", amount)
            print("Your new balance is", balance)

    #option 3
    elif choice == "3":
        amount = float(input("Enter the amount to deposite:"))
        balance += amount
        print("You have deposited", amount)
        print("Your new balance is", balance)

    #option 4
    elif choice == "4":
        new_pin = input("Enter your new 4 digit pin: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            current_pin = new_pin
            print("Your pin has been changed successfully.")
        else:
            print("Invalid pin. Pin must be 4 digits.")

    #option 5
    elif choice == "5":
        print("Thank you for using the ATM. Goodbye!")
    
    #wrong manu options
    else:
        print("Invalid option. Please select a valid option (1-5).")
