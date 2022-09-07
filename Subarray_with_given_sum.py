n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=0
    for j in range(a):
        s=0
        for k in range(j,a):
            s+=c[k]
            if(s==b):
                print(j+1,k+1)
                d=1
        if(d==1):
            break
    if(d==0):
        print(-1)