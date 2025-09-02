print("Good day, Welcome to Elim Bank ")

accounts = [
    {"my_name": "ade", "my_pin": 4529, "account_number": "2287049116", "current_bal": 250000},
    {"my_name": "daniel", "my_pin": 4509, "account_number": "2287078116", "current_bal": 60000},
    {"my_name": "stella", "my_pin": 4519, "account_number": "2287048816", "current_bal": 80000}
]

while True:  # 🔁 Main program loop (this lets you “continue”)
    name = input("\nEnter your name: ").lower()
    for account in accounts:
        if account["my_name"] == name:
            print("\nThank you for banking with us", name.title())
            break
    else:
        print("Sorry, this account does not exist.")
        continue  # go back to start

    balance = account["current_bal"]
    pin = account["my_pin"]

    # PIN Verification
    trial = 4
    print("\nTo verify it's you, kindly input your pin")
    while trial > 0:
        verification = input("Enter PIN: ")
        if verification.isdigit() and int(verification) == pin:
            print("\nWelcome Back", name.title())
            break
        else:
            trial -= 1
            if trial > 0:
                print("You have", trial, "more trials")
            else:
                print("Exiting....trial exhausted!!")
                exit()

    # User Menu
    while True:
        print("\nKindly choose from the options below to proceed\n")
        print("1. Account balance")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Deposit")
        print("Press 5 to continue (restart)")
        print("Press 0 to quit\n")

        choice = input("Select your option (1-5): ")

        if choice == "1":  # Account balance
            print(f"\nYour current balance is: {balance:.2f}")

        elif choice == "2":  # Withdraw
            withdrawal = int(input("\nEnter your desired amount: "))
            if withdrawal > balance - 100:
                print(f"\nInsufficient Funds!! Your current balance is {balance:.2f}")
                print("Kindly note that you must have a minimum of N100")
            else:
                pin_input = input("\nKindly verify with your 4-digits pin or press 0 to cancel: ")
                if pin_input == "0":
                    print("Withdrawal cancelled....returning to menu")
                elif pin_input.isdigit() and int(pin_input) == pin:
                    balance -= withdrawal
                    print(f"\nWithdrawal successful, your new balance is {balance:.2f}")
                else:
                    print("Invalid Pin")

        elif choice == "3":   
            receiver = input("\nEnter Beneficiary account number: ")  
            while True:   
                if receiver.isdigit() and len(receiver) == 10:
                    print("\nBeneficiary account number:", receiver, "\nPlease kindly confirm the account number")

                    while True:
                        passcode = input("\nKindly verify with your 4-digits pin or press 0 to cancel: ")
                        if passcode.isdigit() and len(passcode) == 4 and int(passcode) == pin:
                            amount = float(input("\nEnter the amount you want to send: "))
                            if amount > balance:
                                print(f"\nInsufficient funds! Your current balance is: {balance:.2f}")
                            else:
                                found = False
                                for receiver_acc in accounts:
                                    if receiver_acc["account_number"] == int(receiver):
                                        balance -= amount 
                                        account["current_bal"] = balance
                                        receiver_acc["current_bal"] += amount

                                        print(f"Transfer successful!! You sent {amount:.2f} to account number {receiver}")
                                        print(f"Current balance is = {balance:.2f}")
                                        found = True
                                        break
                                
                                if not found:   # ✅ moved outside the for-loop
                                    print("Transfer failed! Account not found in bank records.")  
                            break   # ✅ exit PIN loop after transfer/checks

                        elif passcode == "0":
                            print("Transfer Cancelled...returning to menu")
                            break
                        else:
                            print("Invalid Pin. Try again or enter 0 to cancel")

                    break  # ✅ exit outer loop after handling transfer or cancel

                elif receiver == "0":
                    print("Returning to menu")
                    break
                else:
                    print("Invalid account number!! Must be 10 digits only.")
                    break


        elif choice == "4":  # Deposit
            deposit = int(input("Enter the amount you are depositing: "))
            if deposit > 100:
                dep_pin = input("Enter your pin: ")
                if dep_pin.isdigit() and int(dep_pin) == pin:
                    balance += deposit
                    print("Deposit successful")
                    print("Your new balance is", balance)
                else:
                    print("Incorrect PIN")
            else:
                print("Deposit must be greater than 100")

        elif choice == "5":  # Restart session
            print("\nRestarting session...\n")
            break  # 🔁 goes back to the main `while True` (login again)

        elif choice == "0":
            print("Thank you for choosing Elim Bank....do have a wonderful day.")
            exit()

        else:
            print("Invalid option, Please read carefully.")