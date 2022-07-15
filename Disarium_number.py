a=int(input())
b=a
a=str(a)
n,c=1,0
for i in a:
    c+=pow(int(i),n)
    n=n+1
if(b==c):
    print('True')
else:
    print('False')