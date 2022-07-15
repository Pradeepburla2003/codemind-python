x=input().lower()
a=[]
for i in  x:
    if(x.count(i)==1 and i!=' '):
        a.append(i)
print(len(a))