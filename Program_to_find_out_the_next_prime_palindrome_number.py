n=int(input())
d=n+1
while(1):
    m=str(d)
    if(m==m[::-1]):
        c=0
        for i in range(2,int(d**0.5)+1):
            if(d%i==0):
                c=1
                break
        if(c==0):
            print(d)
            break
    d=d+1