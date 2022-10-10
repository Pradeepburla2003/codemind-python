n=int(input())
k=bin(n)[2:]
c=0
b=[]
for i in k:
    if(i=='0'):
        b.append(1)
    else:
        b.append(0)
s=len(k)-1
d=0
for i in b:
    if(i==1):
        d+=pow(2,s)
    s=s-1
print(d)