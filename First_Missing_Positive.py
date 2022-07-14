n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
for i in range(1,n+1):
    if i not in a:
        print(i)
        break