def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def modulas(a,b):
    print(a&b)
def squ(a,b):
    print(a**b)

#recursive function
'''def display(s,ind):
    if ind==len(s):
        return 
    print(s[ind])
    display(s,ind+1)
    print(s[ind])

s="PYTHON PROGRAMMING"
display(s,0)
'''
def summ(n):
    if n==0:
        return 0
    return n+summ(n-1)
print(summ(20))
