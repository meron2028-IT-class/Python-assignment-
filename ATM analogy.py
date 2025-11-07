pre_defined_balance = 1000.00

def atm_withdrawal():
    global pre_defined_balance  
    print(f"The current balance is {pre_defined_balance}")
    withdrawal_amount = int(input("Enter the amount of money that you want to withdraw: "))
    
    if withdrawal_amount > pre_defined_balance:
        print("Insufficient funds!")
    elif withdrawal_amount == pre_defined_balance:
        print("Balance will be 0!")
        pre_defined_balance = 0
    elif withdrawal_amount < pre_defined_balance:
        pre_defined_balance -= withdrawal_amount
        print(f"Withdrawal successful! Your new balance is now {pre_defined_balance}")

atm_withdrawal()
