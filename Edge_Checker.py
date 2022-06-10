x,y=map(int,input().split())
if x==y+1 or y==x+1:
    print('Yes')
elif x==1 and y==10:
    print('Yes')
elif y==1 and x==10:
    print('Yes')
else:
    print('No')