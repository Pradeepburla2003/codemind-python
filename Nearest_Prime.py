n=int(input())
for i in range(n):
    a=int(input())
    d=a
    s=a
    if(a==2):
        print('2')
        continue
    while(1):
        c=0
        for k in range(1,d+1):
            if(d%k==0):
                c+=1
        if(c==2):
            m1=d
            break
        d=d-1
    while(1):
        c=0
        a=a+1
        for k in range(1,a+1):
            if(a%k==0):
                c+=1
        if(c==2):
            m2=a
            break
    n1=s-m1
    n2=m2-s
    if(n1<n2):
        print(m1)
    elif(n1==n2):
        print(m1)
    else:
        print(m2)