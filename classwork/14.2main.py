import modules as mo

a=int(input("enter the number"))
b=int(input("enter the number"))

op=input("enter the op(+,-,*,/)")

if op=="+":
    mo.add(a,b)
if op=="-":
    mo.sub(a,b)
if op=="*":
    mo.mul(a,b)
if op=="%":
    mo.modulas(a,b) 
if op=="**":
    mo.squ(a,b)