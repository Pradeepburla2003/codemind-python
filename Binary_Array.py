n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(i!=0 and i!=1):
        c=1
if(c==0):
    print('True')
else:
    print('False')