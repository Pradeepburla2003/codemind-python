x=int(input())
a=list(map(int,input().split()))
d=int(input())
c1=[]
for i in a:
    c=0
    if(i==1):
        continue
    if(i==2):
        c1.append(i)
        continue
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            c=1
            break
    if(c==0):
        c1.append(i)
c=0
for i in c1:
    if(i>=d):
        c+=1
print(c)