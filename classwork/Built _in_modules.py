'''import sys
print("python version",sys.argv)
print("python version",sys.version)
print("python version",sys.path)

a=10
b=20
print(a+b)
sys.exit()
print(a*b)'''

import platform
print(platform.system())
print(platform.release())
print(platform.processor())

import math
print(math.sqrt(24))
print(math.pow(2,8))
print(math.ceil(3.6))
print(math.floor(3.6))
print(math.fabs(3.6))
print(round(3.6))
print(math.factorial(5))
print(math.gcd(12,15))


import random
print(random.random())
print(random.randint(44,77))
print(random.uniform(44,77))
colors=["red",'blue','green']
print(random.choice(colors))