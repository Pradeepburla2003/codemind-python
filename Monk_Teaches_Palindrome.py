x=int(input())
for i in range(x):
    a=input()
    l=len(a)
    k=0
    if(a==a[::-1]):
        k=1
        print('YES',end=' ')
        if(l%2==1):
            print("ODD",end="
")
        else:
            print("EVEN",end="
")
    if(k==0):
        print("NO",end="
")