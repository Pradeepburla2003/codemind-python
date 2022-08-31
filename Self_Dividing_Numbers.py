a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i<10 and i>0):
        print(i,end=' ')
    elif(i%10==0):
        continue
    else:
        c=0
        k=i
        d=str(i)
        for j in d:
            s=int(j)
            if(s==0 or k%s!=0):
                c=1
                break
        if(c==0):
            print(i,end=" ")