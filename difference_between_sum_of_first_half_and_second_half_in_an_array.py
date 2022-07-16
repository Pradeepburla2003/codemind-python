n=int(input())
a=list(map(int,input().split()))
c1,c2=0,0
for i in range(n//2):
    c1+=a[i]
for i in range(n//2,n):
    c2+=a[i]
print(abs(c1-c2))