def prime(s):
    if(s==1):
        return 0
    if(s==2):
        return 1
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
    return 1
n=int(input())
c=0
if(prime(n)):
    while(n>0):
        r=n%10
        c=r+c*10
        n=n//10
    if(prime(c)):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')