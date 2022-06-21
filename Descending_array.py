x=int(input())
a=list(map(int,input().split()))
c=0
for i in range(x-1):
    if(a[i]>a[i+1]):
        c+=1
if(c==x-1):
    print('yes')
else:
    print('no')