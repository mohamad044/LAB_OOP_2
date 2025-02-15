from BankAccount import BackAccount

def bank_program():
    print(" --- Welcome to bank program ---")
    account_holder = input("Enter you accont holder :")
    current_accout = BackAccount(account_holder)
    menu = '''
    choose a service ->
    1. new acount
    2. deposit 
    3. withdraw
    4. display balance 
    5. display account holder
    6. exit
    choise (1:6): '''
    while(True):
        choice = input(menu)
        try:
            if choice == "1":
                account_holder = input("Ente new Account holder: ")
                amount = input("new amount (press enter for default value:0 ): ")
                if amount == "":
                    amount = 0
                current_accout = BackAccount(account_holder,float(amount))
            elif choice == '2':
                amount = input("Enter amout: ")
                current_accout.deposit(float(amount))
                print(f"Added {amount} secssusfuly.\nNew balance is {current_accout.get_balance()}")
            elif choice == '3':
                amount = input("Enter amout to withdraw: ")
                current_accout.withdraw(float(amount))
                print(f"withdraw {amount} secssusfuly.\nNew balance is {current_accout.get_balance()}")
            elif choice == '4':
                print(f"Your balance is {current_accout.get_balance()}")
            elif choice == '5':
                print(f"Your account holder is {current_accout.get_account_holder()}")
            elif choice == '6':
                print("welcome any time again , Thank you !")
                break
            else:
                raise Exception("choose from 1 to 6")
            input("press enter to continue ... ")

        except Exception as e:
            print(e)
            input("press enter to continue ... ")
bank_program()