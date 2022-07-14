x=input().split()
a=min(x[len(x)-1])
b=chr(ord(a)+32)
if b not in x[len(x)-1]:
    print(a)
else:
    print(b)