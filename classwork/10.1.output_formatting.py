# basic print syntax

print("hello world")

#printing multiple items
name="sheshu"
age=22
print("name :", name ,"age :", age)

#c) Using sep to Change the Separator
print("2024","11","01",sep="-")#Instead of spaces, hyphens (-) are used as separators.

#d) Using end to Control Line Endings
print("sheshu",end=" ")
print("reddy")
#Here, end=" " prevents the default new line, and the second print() continues on the same line.
     



# to print in the next line
print("line 1\nline 2")#Output:Line 1 Line 2


#for tab space 
print("name:\tsheshu")

#Output Formatting1️⃣Using Commas (Simple Print Method)
name="sheshu Reddy "
age=22
course="data analysis"

print("name : ",name,"age :","course :",course)

#3️⃣Using f-strings (Formatted String Literals) 

name="sheshu Reddy "
age=22
course="data analysis"
marks=98.88
print(f"name:{name},age:{age},course:{course},marks:{marks:.2f}")
#{score:.2f} → Displays the score with 2 decimal places.

