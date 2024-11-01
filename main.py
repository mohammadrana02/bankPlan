import pandas as pd # pandas will be used of data manipulation and file handling
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
    print('Welcome to the admin dashboard.') # admin dashboard with a number of options
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
        elif option == '2':
            update_admin_info()
        elif option == '3':
            customer_details()
        elif option == '4':
            management_report()
        elif option == '5':
            login_screen()
        else:
            print('Invalid input.')

def customer_options(account_number):
    while True:
        print('Welcome to the customer options screen.') # accessed through the admin dashboard
        print('1. Deposit money into account.')
        print('2. Withdraw money from account.')
        print('3. Check account balance.')
        print('4. View customer details.')
        print('5. Update customer information.')
        print('6. Close the customer account')
        print('7. transfer money to another account')
        print('8. Logout')
        option = input('What would you like to do? ')
        if option == '1':
            deposit = int(input("Enter amount to deposit: "))
            df = pd.read_csv('users.csv')
            #df.loc[df['column_condition'] == value_to_match, 'column_to_update'] = new_value
            df.loc[df['account_number'] == account_number, 'balance'] += deposit # deposits the money into the balance column
            df.to_csv('users.csv', index=False)
            print(f'Deposit successful.')

        elif option == '2':
            withdraw = int(input("Enter amount to withdraw: "))
            df = pd.read_csv('users.csv')
            df.loc[df['account_number'] == account_number, 'balance'] -= withdraw # withdraws money from the balance column
            df.to_csv('users.csv', index=False)
            print(f'Withdraw successful.')

        elif option == '3':
            df = pd.read_csv('users.csv')
            current_balance = df.loc[df['account_number'] == account_number, 'balance']
            print(f'Current balance: {current_balance}') # fix output on this one, not in a clean format

        elif option == '4':
            df = pd.read_csv('users.csv')
            target_user = df[(df['account_number'] == account_number)]

            # looks for the corrects user and outputs all of their information in a clean format
            if not target_user.empty:
                for index, row in target_user.iterrows():
                    for col in df.columns:
                        print(f"{col}: {row[col]}")
                else:
                    print("No matching row found.") # if the user can't be found

        elif option == '5':
            break
        elif option == '6': # drops the row where there account number is, thereby closing the account
            df = pd.read_csv('users.csv')
            df.drop(df[df['account_number'] == account_number].index, inplace=True)

        elif option == '7':
            transfer_to = int(input("Enter the account number you want to transfer to: "))
            transfer_money = int(input("Enter the amount to transfer money: "))
            df = pd.read_csv('users.csv')
            df.loc[df['account_number'] == account_number, 'balance'] -= transfer_money
            df.loc[df['account_number'] == transfer_to, 'balance'] += transfer_money
            df.to_csv('users.csv', index=False)
            print(f'Transfer successful.')
        elif option == '8':
            login_screen()
        else:
            print('Invalid input.')

def update_admin_info():
    pass

def customer_details():
    df = pd.read_csv('users.csv')

    for index, row in df.iterrows(): # outputs all the customer details in an ordered format
        for col in df.columns:
            print(f"{col}: {row[col]}")
        print()

    option = input('Would you like to go back to admin dashboard? (y/n): ')
    if option == 'y':
        admin_screen()
    else:
        login_screen()

def management_report():
    df = pd.read_csv('users.csv')
    total_money = df['balance'].sum() # The sum of all money the customers currently have in their accounts.
    total_overdrafts = df['overdraft'].sum()

    # temporary column to hold the interest for each customer
    df['Interest'] = df['balance'] * df['interest_rate']
    # Calculate the total interest payable
    total_interest_payable = df['Interest'].sum()

    # Display the dataframe and total interest
    print("\n")
    print('Management Report')
    print(f'Total money: {total_money}') # calculates total money in the dataframe
    print(f'Overdrafts: {total_overdrafts}')
    print("Total Interest Payable: ", total_interest_payable)
    print("\n")

    option = input('Would you like to go back to admin dashboard? (y/n): ')
    if option == 'y':
        admin_screen()
    else:
        login_screen()

login_screen()