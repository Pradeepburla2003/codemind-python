x=input().lower()
a=[]
for i in x:
    if(i!=' '):
        a.append(i)
a=sorted(set(a))
for i in a:
    print(i,end="")