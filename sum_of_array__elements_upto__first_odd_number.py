n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(i%2==1):
        break
    else:
        c+=i
print(c)