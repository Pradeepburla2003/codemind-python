n=int(input())
a,b=0,1
c=[]
c.append(a)
c.append(b)
for i in range(n-2):
    d=a+b
    a=b
    b=d
    c.append(d)
if n in c:
    print('True')
else:
    print('False')