import csv
import pandas as pd
pd.set_option('display.max_columns', None) # so the user's data won't be truncated when it is printed to the console

def login_screen():
    print('Welcome to Rana Bank')
    while True: # keeps the user in a loop until they input the correct information
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        login_df = pd.read_csv('users.csv') # converts the csv into a pandas dataframe
        user_exists = login_df[(login_df['username'] == username) & (login_df['password'] == password)] # checks if the username and password match

        if not user_exists.empty: # if the username and the password are a match
            admin_screen()
        else:
            print('Username or password incorrect.') # if they don't match

def admin_screen():
    print('Welcome to the admin dashboard.')
    print('1. Customer search.')
    print('2. Update admin information.')
    print('3. Print all customer details')
    print('4. Request a management report')
    print('5. Logout')
    while True:
        option = input('What would you like to do? Input a number to make a selection: ')
        if option == '1':
            acc_num = int(input("Enter the customer's account number: "))
            customer_options(account_number=acc_num)
            break
        elif option == '2':
            update_admin_info()
            break
        elif option == '3':
            customer_details()
            break
        elif option == '4':
            management_report()
            break
        elif option == '5':
            login_screen()
            break
        else:
            print('Invalid input.')

def customer_options(account_number):
    while True:
        print('Welcome to the customer options screen.')
        print('1. Deposit money into account.')
        print('2. Withdraw money from account.')
        print('3. Check account balance.')
        print('4. View customer details.')
        print('5. Update customer information.')
        print('6. Close customer account')
        print('7. transfer money to another account')
        print('8. Logout')
        option = input('What would you like to do? ')
        if option == '1':
            deposit = int(input("Enter amount to deposit: "))
            df = pd.read_csv('users.csv')
            #df.loc[df['column_condition'] == value_to_match, 'column_to_update'] = new_value
            df.loc[df['account_number'] == account_number, 'balance'] += deposit
            df.to_csv('users.csv', index=False)
            print(f'Deposit successful.')

        elif option == '2':
            withdraw = int(input("Enter amount to withdraw: "))
            df = pd.read_csv('users.csv')
            # df.loc[df['column_condition'] == value_to_match, 'column_to_update'] = new_value
            df.loc[df['account_number'] == account_number, 'balance'] -= withdraw
            df.to_csv('users.csv', index=False)
            print(f'Withdraw successful.')

        elif option == '3':
            df = pd.read_csv('users.csv')
            current_balance = df.loc[df['account_number'] == account_number, 'balance']
            print(f'Current balance: {current_balance}') # fix output on this one
        elif option == '4':
            rows = []
            with open('users.csv', mode='r') as file:
                csv_reader = csv.reader(file)
                # Read and copy all rows into memory
                for row in csv_reader:
                    rows.append(row)

            for r in rows:
                if r[0] == account_number:
                    print('Account Number:', r[0])
                    print('First Name:', r[1])
                    print('Last Name:', r[2])
                    print('Username:', r[3])
                    print('Password:', r[4])
                    print('Address:', r[5])
                    print('Account Type:', r[6])
                    print('Interest Rate:', r[7])
                    print('Balance:', r[8])
                    print('Overdraft:', r[9])
        elif option == '5':
            break
        elif option == '6':
            break
        elif option == '7':
            break
        elif option == '8':
            login_screen()
        else:
            print('Invalid input.')

def update_admin_info():
    pass

def customer_details():
    rows = []
    with open('users.csv', mode='r') as file:
        csv_reader = csv.reader(file)

        # Read and copy all rows into memory
        for row in csv_reader:
            rows.append(row)

    # Convert to DataFrame
    df = pd.DataFrame(rows[1:], columns=rows[0])

    # Display the DataFrame
    print(df)
    option = input('Would you like to go back to admin dashboard? (y/n): ')
    if option == 'y':
        admin_screen()
    else:
        login_screen()

def management_report():
    pass


login_screen()