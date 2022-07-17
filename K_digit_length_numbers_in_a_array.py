x,y=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    j=str(i)
    m=[]
    for k in j:
        if(k.isdigit()):
            m.append(k)
    if(len(m)==y):
        c+=1
print(c)