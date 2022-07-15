x=input().lower()
a=[]
for i in x:
    if(i!=' '):
        a.append(i)
a=list(set(a))
print(len(a))