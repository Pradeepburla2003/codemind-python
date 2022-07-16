n=int(input())
a=list(map(int,input().split()))
i=sum(a)//n
if(i in a):
    print('True')
else:
    print('False')