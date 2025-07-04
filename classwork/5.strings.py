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

#Case Conversion Methods

text1="hello world"

print(text1.upper())#Converts all characters to uppercase

print(text1.lower())#Converts all characters to  lowercase.

print(text1.capitalize()) #Capitalizes the first character.

print(text1.title())#Capitalizes the first letter of each word

print(text1.swapcase()) #Swaps case: upper → lower, lower→ upper.

print(text.casefold()) #Converts to lowercase (more aggressive than lower()).

print(text1.center(19, "*")) #Centers the string within width.

print(text1.ljust(50,"-"))#Left-aligns the string within width.

print(text1.rjust(10,"-")) #right-aligns the string within width

print(text1.zfill(6)) #Pads the string with zeros on the left.

print("name: {}, age: {}".format("sheshu",22)) #Formats strings dynamically.

#Search & Find Methods
print(text1.find("h")) #Returns the index of first occurrence, -1 if not found

print(text1.rfind("h")) #Returns the last occurrence of the substring.

print(text1.index("l")) #Like find(), but raises an error if not found.

print(text1.rindex("l")) #Like rfind(), but raises an error if not found.

print(text1.count("l")) #Counts how many times sub appears.


#4. String Testing Methods (Boolean Results)

print(text1.startswith("he")) #Checks if the string starts with sub.

print(text1.endswith("ld"))#Checks if the string ends with sub.

print(text1.isalpha())#Returns True if all characters are alphabets.

print(text1.isalnum())#Returns True if all characters are alphanumeric.

print(text1.islower())#Returns True if allcharacters are lowercase.


print(text1.isupper())#Returns True if all characters are uppercase.


print(text1.isspace())#Returns True if all characters are whitespace.


print(text1.istitle())#Returns True if the string is in the title case.



print(text1.isidentifier())#Checks if the string is a valid Python identifier.


#5. Replace & Modify Methods

print(text1.replace("h","i"))

print(text1.translate(str.maketrans("e","@")))

print(text1.maketrans("hello","@&%*"))


#6. Splitting & Joining Methods

print(text1.split(" "))#Splits the string into a list by sep

print(text1.rsplit(" "))# Splits from the right side.


print(text1.splitlines(" "))#Splits at line breaks ( ).


result=' '.join(text1)# Joins elements with a separator.
print(result)

text2="hello-world"#Splits into a 3-part tuple at first sep.
print(text2.partition("-"))

print(text2.rpartition("-"))# Splits into a3-part tuple at last sep.

#7. Whitespace & Trimming Methods

print("  hello ".strip()) #Removes leading and trailing characters (default: spaces).

print("----hello".lstrip("-"))#Removes leading characters.

print("hello----".rstrip("-")) #Removes trailing characters.

#8. Encoding & Decoding Methods



