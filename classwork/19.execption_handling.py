try:
    a=9
    b=a+10
    l=[1,3,5]
    d={1:2,3:4,5:6,7:8}
    print(d[9])

except NameError:
    print("name error")
except TypeError:
    print("type error")
except KeyError:
    print("key error")
except IndexError:
    print("index errors")


except (NameError,TypeError,KeyError,IndexError,FileNotFoundError,) as e:
    print(f"error occured{e}")


except Exception as e: # this method is good for all the errors because 
    print(f"error{e}")
else:
    print("no errors")
finally:
    print("code executed sucessfully")


# raise error 
try:
    amount=int(input("enter the amount"))
    if amount<0:
        raise ValueError("enter the positive error")
except Exception as e:
    print(f"error{e}")
else:
    print("no error")

finally:
    print("code executed sucessfully")
