#Tuple Creation Syntax:
empty_tuple = ()
my_tuple = (1, "apple", 3.5)

#2. Accessing Tuple Elements using index

tup=(1,2,3,4,5,6,7)
print(tup[3])

#b. Negative Indexing
tup = (10, 20, 30, 40)
print(tup[-1])

#c. Slicing
tup = (10, 20, 30, 40, 50)
print(tup[1:4])

#3. Operations on Tuples
# a. Concatenation
tup1=(1,2,3,4,5,6)

tup2=(6,4,7,89,0)
mew_tup=tup1+tup2

#b. Repetition 
tup1=(1,2,3,4,5,6)
print(tup1 *4 )

#c. Membership Testing
tup1=(1,2,3,4,5,6)
print(2 in tup1)

#d. Tuple Unpacking
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)

#4. Tuple Methods

(1, 2, 3).count(3)#Counts the number of occurrences of x in the tuple
(1, 2, 3).index(2) #Returns the first index of x in the tuple

#5. Built-in Functions for Tuples
print(len(tup1))

print(max(tup1))
print(min(tup1))

#6. Immutability and Tuple Behavior

nested_tuple = (1, [2, 3])
nested_tuple[1][0] = 100
print(nested_tuple) 

#Dictionary
dictionary_name = {"name":"sheshu",
                  "age": 21,
                    "course": "Computer Science" }

##2.1 Accessing Values
print(dictionary_name["name"])
print(dictionary_name.get("age"))

#2.2 Adding and Updating Items

dictionary_name["age"] = 22 # Updating existing key
dictionary_name["city"] = "New York" # Adding a new key-value pair
print(dictionary_name)

#2.3 Removing Items from a Dictionary
dictionary_name.pop("name")
print(dictionary_name)

#2.3 Removing Items from a Dictionary using del

del dictionary_name["age"]
print(dictionary_name)

#2.3 Removing Items from a Dictionary using popitem
dictionary_name.popitem()
print(dictionary_name)

#3. Dictionary Built-in Methods
dictionary_name.get("course","notfound") #Returns the value for the given key; turns default if key is not found
dictionary_name.keys()# returns al keys in dict
dictionary_name.values() #returns values pf dict