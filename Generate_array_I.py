x=int(input())
a=list(map(int,input().split()))
for i in range(0,x-1,2):
    for j in range(a[i+1]):
        print(a[i],end=" ")