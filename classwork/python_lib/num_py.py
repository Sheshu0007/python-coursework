import numpy as np
arr1=np.array([1,2,3,4,5,6])
print(arr1)

zeros=np.zeros((4,4))
print(zeros)

ones=np.ones((4,4))
print(ones)
# Identity matrix
identity_matrix=np.eye(5)
print(identity_matrix)

# Array of a specific value
fully_array=np.full((9,),7)
print(fully_array)

fuul_array=np.full((2,3),6)
print(fuul_array)

# Array with range of numbers
arr=np.arange(1,8,1)
print(arr)

# Linearly spaced values
lin_space=np.linspace(0,100,500)
print(lin_space)

#2. Random Number Generation

# Random integer values

randominteger=np.random.randint(1,100)
print(randominteger)

hour,minu=map(int,input().split())
print(f"{hour:02d}:{minu:02d}")
