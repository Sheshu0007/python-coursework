

#lambda
lst=[1,2,3,4,5,6,7]
squ=list(map(lambda x:x*x,lst))
print(squ)

for i in lst:
    squa=(lambda x: x*x)(i)
    print(squa)

#filter
lst1=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,lst1))
print(even)

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
stored_students=sorted(students,key=lambda x:x[1])
print(stored_students)

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_grads=dict(sorted(grades.items(),key=lambda x:x[1]))
print(sorted_grads)