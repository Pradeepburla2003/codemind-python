x=int(input())
if(x<3):
    print('The pattern is not possible')
else:
    for i in range(1,x+1):
        for j in range(i):
            print('*',end="")
        print()
    for i in range(x-1,0,-1):
        for j in range(i):
            print('*',end="")
        print()