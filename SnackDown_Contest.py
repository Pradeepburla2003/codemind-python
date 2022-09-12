n=int(input())
for i in range(n):
    d=[]
    a=int(input())
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    b.remove(b[0])
    c.remove(c[0])
    d.extend(b)
    d.extend(c)
    if((len(list(set((d)))))==a):
        print('YES')
    else:
        print("NO")