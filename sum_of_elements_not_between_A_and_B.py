n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
for i in a:
    if(i<b):
        d+=i
    elif(i>c):
        d+=i
print(d)