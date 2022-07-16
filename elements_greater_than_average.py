n=int(input())
a=list(map(int,input().split()))
i=sum(a)//n
c=0
for j in a:
    if(j>=i):
        c+=1
print(c)