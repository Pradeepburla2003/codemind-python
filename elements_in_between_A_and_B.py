x=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
c=0
for i in a:
    if(i>=m and i<=n):
        print(i,end=" ")
        c=1
if(c==0):
    print('-1')