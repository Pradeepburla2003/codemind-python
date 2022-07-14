x=input().lower().replace(' ','')
a=[]
c=0
for i in x:
    if(x.count(i)==1):
        a.append(i)
a=sorted(a)
print(len(a))