#1. String Input
name=input("enter your name :")
print(name)

#2. Integer Input
num=int(input("enter your name : "))

#float input
price=float(input("enter the price "))

#input as list (Space-separated)
names=input("enter tthe names (space-seperated)".split())

#input as list ( comma-seperated)
names=input("enter tthe names (comma-seperated)".split())

#list of integers
l=list(map(int,input("enter the input").split()))

#list of float
l1=list(map(float,input("enter the list of numbers :").split()))

#tuple input
tup=tuple(map(int,input("enter the tuple").split()))

#set input
setsssss=set(map(int,input("enter the set value ").split()))

#dictionary input
dicttt=eval(input("enter the key and values as "))

#multiple inputs and unpacking
username,password=input("enter the username and password :").split()
