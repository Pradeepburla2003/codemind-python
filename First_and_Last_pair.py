n=int(input())
a=list(map(int,input().split()))
if(n%2==1):
    m=n+1
else:
    m=n
b=n-1
for i in range(m//2):
    if(i==b):
        print(a[i],end=" ")
        break
    print(a[i],end=" ")
    print(a[b],end=' ')
    b=b-1
if(n%2==1):
    print('0')