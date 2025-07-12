# CONDITIONAL STATEMENTS
# IF STATEMENTS
num=3
if num<=5:
    print("the number is greater then num")

else:
    print("it is not")


#EXAMPLE
status_signal=input("enter the status of signel: ")
if status_signal=="R":
    print("stop")
elif status_signal=="orange":
    print("ready")
else:
    print("go")




# example 2


items=["laptop","mobile","palystation","xbox"]

print("welcome to the amazon store".center(50,"#"))\

search_input=input("enter the item:".lower())

if search_input in items:
    print(f"{search_input} found.buy now")

else:
    print("the product is out of stock")


#weekend budget plan
amount=int(input("Enter the amount you wanted to spend"))

if amount>100000:
    print("international trip")

elif amount>50000:
    print("trip to goa")

elif amount>25000:
    print("shopping")
elif amount>15000:
    print("earn more money")

elif amount>100:
    print("sleep")
     

else:
    print("have a proper sleep then find some work or do somthing")
     

#example 3
#gradeing


num=int(input("enter the number :"))
if num<0:
    print("its a positive number ")

elif num>0:
    print("its a negative number :")

else:
    print("its a zero")



    num=int(input("enter the number :"))
if num>0:
    print("its a positive number ")

elif num<0:
    print("its a negative number :")

else:
    print("its a zero")



num=int(input("enter the number :"))
if num%2==0:
    print(f"{num}is a even number")
else:
    print(f"{num}is a odd number")



num=int(input("enter the number :"))
if num%3 & num%5==0:
    print(f"{num}is divisible by 3 and 5 ")

else:
    ("f{its not divisible by 3 and 5}")

    