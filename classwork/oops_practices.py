#1. Book Details DisplayProblem: Create a Book class with title, author, and price. Add a method to display all book details.
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print(f"title:{self.title},author:{self.author},price{self.price} ")

p1=Book("movie","sheshu",900)
p1.display()        

#Problem: Create an Employee class with name, base_salary. Add a method calculate_annual_salary.
class employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def employe_details(self):
        print(f"{self.name},{self.base_salary}")

    def display1(self):
        print(f"anual salary={self.base_salary*12}")
e1=employee("sheshu",20000)
e1.employe_details()
e1.display1()

#3. Student Grade Evaluator Problem: Create a Student class with a list of marks. Add a method to return average and pass/fail.
class grade_evaluator:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def caluclater(self):
        avg=sum(self.marks)/len(self.marks)
        if avg>40: 
            print("pass")
        else:
            print("fail")
s1=grade_evaluator("sheshu",[30,44,30])
s1.caluclater()

#Problem: Create a BankAccount class with deposit, withdraw, and balance display.
class Bankaccout:
    def __init__(self):
        self.balance=1000
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("low balance")
    def check_balance(self):
        print(f"{self.balance}")
u1=Bankaccout()
u1.withdraw(500)
u1.check_balance()
u1.deposit(555)
u1.check_balance()

