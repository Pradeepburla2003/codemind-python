x=set(input().lower().replace(' ',''))
y=set(input().lower().replace(' ',''))
c=0
a=[]
for i in x:
    if i in y:
        a.append(i)
        c=1
if(c==0):
    print('-1')
else:
    a=sorted(a)
    for i in a:
        print(i,end="")