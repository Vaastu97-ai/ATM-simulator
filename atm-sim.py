print('Welcome to the ATM Simulator')
balance = int(input("Enter your initial balance: "))
pin = int(input("Set your PIN: "))
chances = 3  # number of attempts

while chances > 0:
    enter_pin = int(input('Enter your PIN: '))
    
    if enter_pin == pin:
        print("PIN is correct")

        while True:
            print('\n*** ATM MENU ***')
            print('1. Check Balance')
            print('2. Deposit Money')
            print('3. Withdraw Money')
            print('4. Exit')

            choice = int(input('Enter your choice: '))

            if choice == 1:
                print('Your balance is:', balance)

            elif choice == 2:
                deposit = int(input('Enter amount to deposit: ₹'))
                balance += deposit
                print('Deposited successfully! New balance = ₹', balance)

            elif choice == 3:
                withdraw = int(input('Enter amount to withdraw: ₹'))
                if withdraw > balance:
                    print('Insufficient funds!')
                else:
                    balance -= withdraw
                    print('Withdrawn successfully! Remaining balance = ₹', balance)

            elif choice == 4:
                print('Thank you for using the ATM!')
                break

            else:
                print('Invalid choice, please try again.')

        break  # exit main loop after successful session

    else:
        chances -= 1
        print('Incorrect PIN! Attempts left:', chances)
        if chances == 0:
            print('Your account is blocked!')