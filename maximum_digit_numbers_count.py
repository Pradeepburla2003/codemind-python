n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    j=len(str(i))
    b.append(j)
m=max(b)
for i in a:
    j=len(str(i))
    if(j==m):
        print(i,end=" ")