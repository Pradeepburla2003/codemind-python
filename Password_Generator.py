x=input().split(',')
for i in x:
    j=i.split(':')
    k=[]
    m=0
    t=j[0]
    d=len(j[0])
    for s in j[1]:
        k.append(int(s))
    while(1):
        if d in k:
            print(t[d-1],end="")
            m=1
            break
        elif(d-1==0):
            break
        else:
            d=d-1
    if(m==0):
        print('X',end="")