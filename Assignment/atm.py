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

def Check_Balance():
    if login_status and acc_num:
        print(f"Current balance:{data[acc_num]["balance"]}")
    else:
        print("you need to login again")

def Withdraw():
    if login_status and acc_num:
        amount=int(input("enter the amount to withdraw"))
        if data[acc_num]["balance"]>=amount:
            data[acc_num]-=amount
            data[acc_num]["history"]