a,b=map(int,input().split())
for i in range(min(a,b),(a*b)+1):
    if(i%a==0 and i%b==0):
        print(i)
        break