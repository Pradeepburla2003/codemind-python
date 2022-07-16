n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
m=0
d=[]
for i in a:
    if(i<b):
        d.append(i)
        m=1
    elif(i>c):
        d.append(i)
        m=1
if(m==0):
    print('-1')
else:
    print(max(d))