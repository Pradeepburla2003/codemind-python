x=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
c=0
for i in a:
    if(i>=m and i<=n):
        c+=i
print(c)