x=input().split()
for i in x:
    a=[]
    j=str(i)
    for k in j:
        if(k.isdigit() or k.isalpha()):
            a.append(k)
    a=sorted(a)
    m=0
    for k in j:
        if(k.isdigit() or k.isalpha()):
            print(a[m],end="")
            m+=1
        else:
            print(k,end="")
    print(' ',end="")