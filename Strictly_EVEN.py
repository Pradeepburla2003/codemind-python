n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in range(n):
    if(a[i]%2==0):
        if(i%2!=0):
            c=1
            break
if(c==0):
    print('True')
else:
    print('False')