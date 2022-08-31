n=int(input())
a=0
for i in range(1,(n//2)+1):
    if(n%i==0):
        k=n//i
        if(i==k-1):
            print('YES')
            a=1
            break
if(a==0):
    print('NO')