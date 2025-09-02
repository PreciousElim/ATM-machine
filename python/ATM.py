print("Good day, Welcome to Elim Bank ")

accounts = [
    {"my_name": "ade", "my_pin":4529, "account_number": 2287049116, "current_bal" :250000},
    {"my_name": "daniel", "my_pin":4509, "account_number": 2287078116, "current_bal" :60000},
    {"my_name": "stella", "my_pin":4519, "account_number": 2287048816, "current_bal" :80000}
]

name = str(input("Enter your name: ").lower())
#Allow's you to in put names, either ade,stella or daniel
for account in accounts:
    if account["my_name"] == name:
        print("\nThank you for banking with us", name.title())
        #The (.title) makes the name written to be in a proper form if it wasn't
        break
else:
    print("Sorry, this account does not exist.")
    exit()

balance = account["current_bal"]
receivers_bal =account["current_bal"]
pin = account["my_pin"]
account_no =account["account_number"]


trial = 4
print("\nTo verify it's you, kindly input your pin")
while trial > 0: 
    
    verification = int(input("Enter PIN: "))

    if pin == verification:
        print("\nWelcome Back", name.title())
        break
    else:
        trial -= 1
        if trial > 0:
            print("You have", trial , "more trials")
        else:
            print("Exiting....trial exhusted!!")            
            exit()  

              
while True:
    print("\nKindly choose from the options below to proceed\n")
    print("1. Account balance")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Deposite")
    print("press 5 to continue")
    print("Press 0 to quit\n")

    choice = str(input("Select your option(1-5): "))

    if choice == "1":
        print(f"\nYour current balance is: {balance:.2f}" )
        

    elif choice== "2":
        withdrawal =int(input("\nEnter your desired amount: "))
        if withdrawal > balance - 100:
            print(f"\nInsufficient Funds!! Your current balance is {balance:.2f}")
            print("Kindly note that you must have a minimun of N100")

        else:
            while True:
                if withdrawal < balance - 100:

                    Pin = input("\nKindly verify with your 4-digits pin or press 0 to cancel: ")
                    if Pin =="0":    
                            print("Withdrawal cancelled....returning to menu")
                            print("Thank you for banking with us")
                            break
                    
                    if Pin.isdigit() and len(Pin) == 4 and  int(Pin) == pin:
                        balance -= withdrawal
                        print(f"\nWithdrawal successful, your new balance is {balance:.2f}" )     
                        break
                    else:
                        print("Invalid Pin... Try again or press 0 to cancel: ")
                
    elif choice == "3":   
         receiver = input("\nEnter Beneficiary account number: ")  
         while True:
            if receiver.isdigit() and len(receiver) == 10 :
                print("\nBeneficiary account number:", receiver, "\nPlease kindly confirm the account number")
                passcode = input("\nKindly verify with your 4-digits pin or press 0 to cancel: ")
                if passcode.isdigit() and len(passcode)== 4 and int(passcode) == pin :                 
                    amount = float(input("\nEnter the amount you want to send: "))

                    if amount > balance:
                        print(f"\ninsufficent funds your current balance is: {balance:.2f}")

                    else:   

                        for receiver_acc in accounts:

                            if receiver_acc["account_number"] == int(receiver):
                                balance -= amount 
                                account["current_bal"] = balance
                                receiver_acc["current_bal"] += amount
                                print(f"Transfer successful!! You sent {amount:.2f} to account number", receiver)
                                print(f"Current balance is = {balance:.2f}")
                                break
                    break       
                elif passcode == "0":
                    print("Transfer Cancelled...returning to menu")
                    break
                else:
                    print("Invalid Pin. Try again or enter 0 to cancel")


            elif receiver == "0":
                print("Returning to menu")
                break
                

            else:
                print("Invalid account number!! Must be 10 digits only.")
                break

    elif choice == "4":
        print("Good day", name.title(), "how much would you be deposting today")
        deposit = int(input("Enter the amount you are depositing: "))
        while True:
             
             if deposit > 100: 
                    dep_pin = input("Enter your pin: ")

                    if dep_pin.isdigit() and int(dep_pin) == pin:
                        balance += deposit
                        print("Deposit successful")
                        print("Your new balance is", balance)
                        break
                    else:
                        print("Incorrect PIN")
             else:
                print("Deposit must be greater than 100")
                

    elif choice == "5":
        print("\nChoose again.... ")
        break
        
        
    elif choice == "0":
        print("Thank you for choosing Elim bank....do have a wonderfull day.")   
        exit()
        
        
    else:
        print("Invalid digit, Try again")   