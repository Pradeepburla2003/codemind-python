n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for j in range(a):
        for k in range(j+1,a):
            if(b[j]+b[k] in b):
                c+=1
    if(c==0):
        print(-1)
    else:
        print(c)