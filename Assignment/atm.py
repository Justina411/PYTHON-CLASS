def atm_simulator():
    balance = 1000 

    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is: ${balance}")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                if amount > 0:
                    balance += amount
                    print(f" Deposit successful! New balance: ${balance}")
                else:
                    print("Invalid deposit amount.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                if amount <= 0:
                    print("Invalid withdrawal amount.")
                elif amount > balance:
                    print("Insufficient funds!")
                else:
                    balance -= amount
                    print(f"Transaction successful! New balance: ${balance}")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break  

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

# Run the ATM simulator
atm_simulator()
