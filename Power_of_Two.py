n=int(input())
if(n%2==1):
    print('False')
else:
    while(n>0):
        if(n==2):
            print('True')
            quit()
        if(n%2==0):
            n=n//2
        else:
            print('False')
            quit()