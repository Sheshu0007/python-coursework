# multiplication using the for loops


num=int(input("Enter the table number :"))

for i in range(1,21):
    print(f"{num}*{i}={num*i}")
    

s="sheshu supriya tejaswini ashajyothi".lower()

ch=(input("Enter the char:".lower()))

for i in range(len(s)):
    if s[i]==ch:
        print(ch,i)




products=["ps5","cycle","bike","car"]

items=input("enter the product name:").lower()

for i in items:
    if i in products:
        print(products.index(i),i)
    else:
        print("the item is not available")  



user,pwd="zyz@gmail.com","1234"
max_attemts=5

while max_attemts>0:
    email=input("enter the email")
    passw=input("enter thye password")
    if user==email and passw==pwd:
        print("succesfully login")
        break
    else:
        print("invalid email or password")
    max_attemts-=1

else:print("try after some time")



'''for row in range(5):
    for col in range(5):
        print("*",end=" ")
    print()

for row in range(5):
    for col in range(5):
        print(col,end=" ")
    print()

for row in range(5):
    for col in range(5):
        print(row,end=" ")
    print()
'''

print("welcome to grocery store ".center(50,"-"))
print("here are the availble product:")
grocery={
    1:{"name":"rice","price":50},
    2:{"name":"peper","price":33},
    3:{"name":"milk","price":33},
    4: {"name": "Wheat Flour", "price": 40.0},
    5: {"name": "Sugar", "price": 45.0},
    6: {"name": "Milk", "price": 25.0},
    7: {"name": "Oil", "price": 130.0},
    8: {"name": "Soap", "price": 30.0},
    9: {"name": "Shampoo", "price": 90.0},
    10: {"name": "Eggs (dozen)", "price": 60.0},
    11: {"name": "Salt", "price": 20.0},
    12: {"name": "Tea Powder", "price": 150.0}
}
 
for i in grocery:
    print(f"{i}. {grocery[i] ['name']} - {grocery[i]['price']}")

items=list(map(int,input("enter the product index num(1 2 3 4 5)").split()))
total=0
s=set()
for i in items:
    if i not in s:
        c=items.count(i)
        print(f'{grocery[i]["name"]} - {c}*${grocery[i] ["price"]}=${c*grocery[i]["price"]}')
        total+=grocery[i] ["price"]*c
        s.add(i)
print(f'Total bills: {total}')