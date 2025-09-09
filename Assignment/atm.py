data={
    12345:{'pin':123,'balance':5678,'history':[]},
    23456:{'pin':123,'balance':5678,'history':[]},
    67891:{'pin':123,'balance':5678,'history':[]},
    98765:{'pin':123,'balance':5678,'history':[]},
    45674:{'pin':123,'balance':5678,'history':[]},
    36783:{'pin':123,'balance':5678,'history':[]},
    }

acc_num=None
login_status=None

def welcome():
    print("welcome to the ATM".center(50,"-"))

def login():
    account_no=int(input("enter the the account number:"))
    pin=int(input("enter the pin number:"))
    if account_no in data:
        if data[account_no]["pin"]==pin:
            print("Login Successful")
            acc_num==account_no
            login_status==True
            return True
        else:
            print("invalid")
            login_status=False
            return False
    else:
        print("invalid account number")
        login_status=False
        return False
def menu():
    print('\n[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit\n')

def deposit():
    if login_status and acc_num:
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            data[acc_num]["balance"] += amount
            data[acc_num]["history"].append(f"Deposited {amount}")
            print(f"✅ {amount} deposited successfully!")
        else:
            print("⚠️ Invalid amount.")
    else:
        print("⚠️ You need to login again.")


# Withdraw
def withdraw():
    if login_status and acc_num:
        amount = int(input("Enter the amount to withdraw: "))
        if amount > 0 and data[acc_num]["balance"] >= amount:
            data[acc_num]["balance"] -= amount
            data[acc_num]["history"].append(f"Withdrew {amount}")
            print(f"✅ {amount} withdrawn successfully!")
        else:
            print("⚠️ Insufficient balance or invalid amount.")
    else:
        print("⚠️ You need to login again.")


# View Transactions
def view_transactions():
    if login_status and acc_num:
        print("\n📜 Transaction History:")
        if data[acc_num]["history"]:
            for t in data[acc_num]["history"]:
                print("-", t)
        else:
            print("No transactions yet.")
    else:
        print("⚠️ You need to login again.")


def Exit():
    print("Thank you for using the ATM. Goodbye!")
    exit()



    # A= write a different types of program snd with function in another file 
    