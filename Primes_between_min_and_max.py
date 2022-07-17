n=int(input())
a=list(map(int,input().split()))
b,c=min(a),max(a)
for i in range(n):
    if(a[i]==b):
        d=i
    if(a[i]==c):
        f=i
if(d>f):
    d,f=f,d
s=0
for i in range(d,f+1):
    k=0
    if(a[i]==1):
        continue
    for j in range(2,int(a[i]**0.5)+1):
        if(a[i]%j==0):
            k=1
            break
    if(k==0):
        s+=1
print(s)