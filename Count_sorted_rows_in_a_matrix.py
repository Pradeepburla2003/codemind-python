x,y=map(int,input().split())
c=0
for i in range(x):
    a=list(map(int,input().split()))
    b=sorted(a)
    if(a==b or a==b[::-1]):
        c+=1
print(c)

