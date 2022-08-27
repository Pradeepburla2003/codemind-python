n=int(input())
a=list(map(int,input().split()))
for i in a:
    j=i
    if(j<0):
        s=0
        j=-i
        while(j>0):
            r=j%10
            s=s*10+r
            j=j//10
        print(-s,end=" ")
    else:
        s=0
        while(j>0):
            r=j%10
            s=s*10+r
            j=j//10
        print(s,end=" ")
          