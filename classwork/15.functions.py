def sum_of_digits(n):
    if n == 0:
        print("Reached base case, returning 0")
        return 0
    else:
        last_digit = n % 10
        remaining = n // 10
        print(f"At n={n}: last_digit={last_digit}, remaining={remaining}")
        
        result = last_digit + sum_of_digits(remaining)
        print(f"Returning {result} for n={n}")
        return result

# Example
print("Final Answer:", sum_of_digits(1234))
def greet(name):
    print(f'{name} welcome')
greet("sheshu")

def addition(a,b):
    return a+b
print(addition(4,6))

def greet1(name="guest"):#If no value is passed, default is used.
    print(f'{name} welcome')
greet1()

# Keyword Arguments
def greet2(name,age):
    print(f"The person name is {name} and the age is {age}")
greet2("sheshu",23)

#Local Scope 
def greet3():
    msg="sheshu"
    print(msg)
greet3()


#global variable and update
messag="hello"
def outter():
   global messag
   messag="hi"
outter()
print(messag)

#enclosing scope
def outter1():
    mssg=10
    def inner():
        print(mssg)
        
        inner()
outter1()

#nonlocal
def outter1():
    mssg=10
    def inner():
        nonlocal mssg
        print(mssg)
        
        inner()
outter1()


def outer():
    msg2 = "Hi"
    print(msg2)
    def inner():
        nonlocal msg2
        msg2="hello"
        print(msg2) # Enclosing scope variable is found in enclosing scope area to update the enclosing scope variable we need to update the variable into nonlocal because the msg is not local for inner function
    inner()
    print(msg2)
outer()
#global x = "global"
x="global"
def outer():
    global x
    x="global1"
    print(x)
    def inner():
        x = "local"
        print(x) # Looks for local, enclosing, global,
    inner()
outer()
print(x)


#recursive functions
def sum_1(n):
    if n==0: 
        return 0
    else:
        return n + sum_1(n-1)
print(sum_1(5))

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

def modify_list_copy(lst):
    lst = lst[:] # Creates a copy
    lst.append(5)
    print("Inside function:", lst)

numbers = [1, 2, 3]
modify_list_copy(numbers)
print("Outside function:", numbers)







def summ(n):
    if n==1:
        return 1
    return n * summ(n-1)
print(summ(5))


def display(s,ind):
    if ind==len(s):
        return 
    display(s,ind+1)
    print(s[ind],end="")



def feb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else : return feb(n-1)+feb(n-2)
print(feb(7))

def sumofdig(n):
    if n==0:
        return 0
    return (n%10)+sumofdig(n//10)
print(sumofdig(1234))

def countofnum(n):
    if n==0:
        return 0
    return 1+countofnum(n//10)
print(countofnum(1234))


class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        print(first,last)
    
    def bonus(self):
        self.pay=int(self.pay * 40)

emp1=employee("sheshu","reddy",3000) 
emp1.bonus()   
print(emp1.pay)