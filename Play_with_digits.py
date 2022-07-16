n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    j=str(i)
    for k in j:
        c+=int(k)
print(c)