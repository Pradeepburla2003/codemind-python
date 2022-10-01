n=int(input())
for i in range(n):
    a=input()
    k=0
    j=len(a)-1
    for l in a:
        if(l=='1'):
            k=k+pow(2,j)
        j=j-1
    print(k)