a=int(input())
c=1
for i in range(2,(a//2)+1):
    if(a%i==0):
        c+=i
if(c<a):
    print('False')
else:
    print('True')