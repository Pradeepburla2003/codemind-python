n=int(input())
a=list(map(int,input().split()))
b=0
for i in a:
    if(i%2==0):
        break
    b+=i
print(b)