n=int(input())
for i in range(n):
    a=int(input())
    b=list(str(a))
    d=int(min(b))
    f=int(max(b))
    c=0
    for i in range(d+1,f):
        j=str(i)
        if j not in b:
            c=1
            break
    if(c==0):
        print('YES')
    else:
        print('NO')