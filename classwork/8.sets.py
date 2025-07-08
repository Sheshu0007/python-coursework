#Sets
# Creation Syntax:
myset=set()

myset1={1,2,3,4,5,6}

#Operations on Sets
myset1={1,2,3,4,5,6}
print(2 in myset)

#b. Union (| or union() method)
myset2={3,4,5,6,7,8}
result=myset1 | myset2

#c. Intersection (& or intersection() method)
intersection1=myset1 & myset2


# d. Difference (- or difference() method)
Difference_method=myset1 - myset2

#e. Symmetric Difference (^ or symmetric_difference() method)
Symmetric_Difference=myset1^myset2

#f. Subset (<= or issubset() method)
Subset_methods=myset1<=myset2

#g. Superset (>= or issuperset() method)
Superset_method=myset1>=myset2

#h. Disjoint Sets (isdisjoint() method)
myset1.isdisjoint(myset2)


#4. Built-in Methods for Sets
myset1.add(55) # adding the element to the set

myset1.remove(4) # removes the 4 from the set

myset1.discard(4) # Removes an element; does notraise an error if the element doesn’t exist

myset1.pop() # remoes random element from the set

myset1.clear() # Removes all elements from the set

myset1.update(myset2) #Adds elements from another set to the current set

myset1.intersection_update(myset2) #Updates the set with theintersection of itself and another set

myset2.difference_update(myset1) #Updates the set by removing elements found in another set

myset1.symmetric_difference_update(myset2) #Updates the set with the symmetric difference

#5. Built-in Functions for Sets
len(myset2) #Returns the number of elements in the set

max(myset2) #Returns the maximum element in the set


min(myset2) #Returns the minimum element in the set

sum(myset2) #Returns the sum of all elements in the set

sorted(myset2) # Returns a sorted list of the set elements

