# List
'''Basic Features of Lists
● Ordered: Lists maintain the order of elements.
● Mutable: Elements can be modified after creation.
● Indexed: Elements can be accessed using an index (starting from 0).
● Allow Duplicates: Lists can contain duplicate values.
● Heterogeneous: Lists can contain different data types (e.g., int, str, float, etc.).
● Dynamic: Size is not fixed; elements can be added or removed dynamically.'''

#2. Creating Lists
my_list=[] #empty list

#2.2 List with Elements
num=[1,2,3,4,5,6,7,8,9]
names=["sheshu","friend","enemy"]

#2.3 List with Nested Lists
num=[[1,2,3][4,5,6][6,7,8]]

#2.4 List using list() Constructor
num1=list(1,2,3,4,5)
string_to_list=list("python")

#3. Accessing Elements in a List
#3.1 Using Indexing (Positive & Negative)
text=["sheshu",22,2.4]
print(text[0])
print(text[1])
print(text[-1])


#3.2 Using Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:5])
print(numbers[-3:-1])
print(numbers[::-1])#revers list

#4. Modifying Lists
numbers[2]=100
print(numbers)

#4.2 Adding Elements
numbers.append(1000) ## Append (adds to the end)
numbers.insert(1,7)# add at a specfice position
numbers.extend([60,33,22]) # adds multiple values at the end

#4.3 Removing Elements
numbers.remove(1000)# removes the firdt occurrence of 1000
numbers.pop()# removes the last element
numbers.pop(2)# removes the element at index 2
del numbers[1]# deletes the elements at index 1
numbers.clear() # clear the entire list
