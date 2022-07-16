n=int(input())
a=list(map(int,input().split()))
a=a[::-1]
for i in a:
    if(i%2==0):
        print(i)
        break