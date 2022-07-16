x=input().split()
ch='aeuioAUIOE'
for i in x:
    a=[]
    j=str(i)
    for k in j:
        if k not in ch:
            a.append(k)
    a=sorted(a)
    m=0
    for k in j:
        if k not in ch:
            print(a[m],end="")
            m+=1
        else:
            print(k,end="")
    print(' ',end="")