n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in range(0,n-2,2):
    if(a[i]<a[i+1] and a[i+1]>a[i+2]):
        c+=1
    elif(a[i]>a[i+1] and a[i+1]<a[i+2]):
        c+=1
    else:
        k=1
        break
if(k==0):
    print('yes')
else:
    print('no')