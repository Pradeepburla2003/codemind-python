n=int(input())
a=list(map(int,input().split()))
c,d=0,0
for i in range(n-1,-1,-1):
    if(a[i]==1):
        c+=pow(2,d)
    d=d+1
print(c)