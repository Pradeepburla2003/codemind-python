n=int(input())
a=list(map(int,input().split()))
c=0
j=0
for i in range(n):
    if a[i]==1:
        j+=1
    else:
        c=max(c,j)
        j=0
c=max(c,j)
print(c)