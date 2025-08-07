photos={
    1:"mount.jpg",
    2:"villages.jpg",
    3:"home.jpg",
    4:"college.jpg",
    5:"hostel.jpg",
    6:"school.jpg"
}

for key,value in photos.items():
    print(f'{key}:{value}')

number_pic=set(map(int,input("enter the numbers:").split(",")))
print("Sharing the following photos")

for i in photos:
    print(f'')
"""for num in number_pic:
    if num in number_pic:
        print(f'{num}={photos[num]}')
    else:
        print("invalid number")"""

""""for i in data:
    print(f'{i}.{data[i]}')
l=set(map(int,input("enter the numbers:").split(",")))
for i in l:
    print(f'{data[i]} - sharing the images')"""
    