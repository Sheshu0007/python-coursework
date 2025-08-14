def circle_geometry(r):
    area=3.127*(r*r)
    circum=2*(3.127)*(r*r)
    return area, circum
circle_geometry(7)

import random
team=[1,2,3,4,5,6,7,8]
pick=random.sample(team,2)
print(pick)


lst2=[34,56,23,44,33,45]
temp=list(filter(lambda x: x>40,lst2))
print(temp)


lst3=["cat", "car", "bat", "apple"]
fst=list(filter(lambda x:x[0]=="c",lst3))
print(fst)

def is_palindrome(word):
    word1=word[::-1]
    if word==word1:
        print(True)
    else:
        print(False)

def capatilize(text):
    print(text.title())



capatilize("hello world")
is_palindrome("madam")

lst4=["Apple", "apple", "Banana", "BANANA", "Cherry"]
remove_duplicate=set(filter(lambda x:x,lst4))
print(remove_duplicate)


x=list(map(int,input()))
print(x)