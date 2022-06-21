x=int(input())
a=list(map(int,input().split()))
c=0
for i in range(x):
    s=0
    for j in range(1,a[i]+1):
        if(a[i]%j==0):
            s+=1
    if(s==2):
        c+=1
print(c)