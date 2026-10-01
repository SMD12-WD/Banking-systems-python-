balance = 2000
Name = input("Please provide your Full Name: ").upper()
user_choice = input(f'''Welcome {Name} what are you looking to do today
1. Check balance
2. Deposit
3. Withdraw
4. Exit     
'''
)
if user_choice == "1":
    print(f"Your balance is: R{balance}")

if user_choice == "2":
    amount = input("Amount to deposit: R ")
    balance += int(amount) # Update the actual balance variable so the new amount is saved for future transactions
    print(f"Successfully deposited {amount}")
    print(f"your new balance is: R{balance} ")

if user_choice == "3":
    amount_withdraw = int(input("Amount to withdraw: R "))
    if amount_withdraw > balance:
        print("Insufficient funds")
    else:
        balance -= amount_withdraw
        print(f'''Withdrawal successful!
Your new balance is: R{balance}''')
















