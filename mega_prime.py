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
a=list(str(n))
c=0
if(prime(n)):
    for i in a:
        j=int(i)
        if(prime(j)):
            c+=1
    if(c==len(a)):
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')