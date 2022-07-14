a=input().lower()
b=[]
for i in a:
    if(i!=' '):
        b.append(i)
b=sorted(set(b))
for i in b:
    print(i,end="")