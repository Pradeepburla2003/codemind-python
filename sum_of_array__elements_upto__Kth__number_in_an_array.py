n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in range(b):
    c+=a[i]
print(c)