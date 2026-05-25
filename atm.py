pin = "1234"
balance = 1000
mini_statement = []

def authenticate():
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print("Authentication is successful.")
        return True
    else:
        print("Incorrect PIN.")
        return False
    
def atm_system():
    global balance, pin
    while True:
        print("\n============ATM MENU============")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Mini Statement")
        print("6. Exit")
        print("=============================")

        choice = input("Enter your choice: ")

        #check balance
        if choice == "1":
            print(f"current balance: ${balance}")
            mini_statement.append(f"check balance: ${balance}")

        #deposit money
        elif choice == "2":
            amount = float(input("enter the amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"${amount} deposited successfully.")
                mini_statement.append(f"deposit: ${amount}")
            else:
                print("Invalid amount. ")
        #withdraw money
        elif choice == "3":
            amount = float(input("enter the amount to withdraw: "))
            if amount > 0:
                balance -= amount
                print(f"${amount} withdrawn successfully.")
                mini_statement.append(f"withdraw: ${amount}")
            else:
                print("Invalid amount. ")
        #change pin
        elif choice == "4":
            old_pin = input("enter your old pin: ")
            if old_pin == pin:
                new_pin = input("enter your new pin: ")
                confirm_pin = input("confirm your new pin: ")
                if new_pin == confirm_pin:
                    pin = new_pin
                    print("Pin changed successfully.")
                    mini_statement.append("change pin: success")
                else:
                    print("pin mismatch.")
            else:
                print("incorrect old pin.")
        #mini statement
        elif choice == "5":
            print("\nMini Statement:")
            for transaction in mini_statement:
                print(transaction)
        #exit
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break


if __name__ == "__main__":
    if authenticate():
        atm_system()