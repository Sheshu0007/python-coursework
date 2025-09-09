import re
res=re.match("a","abcd")
print(res.group() if res else "no match")

RES1=re.match(r"[A-Z]","123svb")
print(RES1.group() if RES1 else "not matched")

RES2=re.match(r"[A-Z]","svb")
print(RES2.group() if RES2 else "not matched")

RES3=re.match(r"[A-Z]","W")
print(RES3.group() if RES3 else "not matched")

res4=re.search(r"[a-z]+","123dkofemjRDD")
print(res4.group() if res4 else "not  found")

res5=re.findall(r"[a-z]","123dkofemjRDD")
print(res5 if res5 else "not  found")

res6=re.finditer(r"[1-9]","12 45 85 dsds drr4")
print(res6)
for i in res6:
    print(i.group(),i.start())


res7=re.fullmatch(r"[a]+","aaaaaaaaaaaaa")
print(res7.group() if res7 else "not full match")