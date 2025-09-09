'''a=5
b=0
try:
    solution=a/b
except ZeroDivisionError:
    print("cannot divide")
else:
    print(solution)'''


'''a=[1,2,3,4,5]
try:
    lst=a[5]
except Exception as e:
    print(e)
else:
    print(lst)'''

'''import re
res=re.match(r"[6-9][0-9]{9}$","9876543210")
print(res.group() if res  else "no match")'''