n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    j=str(i)
    if(j==j[::-1]):
        c+=1
print(c)