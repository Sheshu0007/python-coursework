A='hello '
B="world"
C='''hello
 world'''# it is used for multi lines
print(A)
print(B)
print(C)

#CONCATENATION
RESULT=A+" "+B
print(RESULT)# ADDING THE 2 STRINGS

#REPETITION
print(A*3)#output= hello hello hello

-
#INDEXINGxz/x
text = "helloword"
print(text[0])
print(text[5])

#SLICING
print(text[0:8])

#membership 
print("hello" in text)
print("hiii" in text)


#built in string Functions
print((len(text)))#len() - Returns the length of the string.

print(max(text)) #- Returns the maximum character (based on ASCII values).
print(min(text))#Returns the maximum or minimum character (based on ASCII values).
print(sorted(text)) #- Returns a sorted list of characters.
