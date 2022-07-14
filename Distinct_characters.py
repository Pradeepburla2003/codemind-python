x=input().lower().replace(' ','')
a=[]
c=0
for i in x:
    if(x.count(i)==1):
        a.append(i)
a=sorted(a)
for i in a:
    print(i,end="")