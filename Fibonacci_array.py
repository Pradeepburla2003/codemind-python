n=int(input())
a=list(map(int,input().split()))
if(n<3):
    print('no')
else:
    for i in range(2,n):
        if(a[i]!=a[i-1]+a[i-2]):
            print('no')
            break
    else:
        print('yes')