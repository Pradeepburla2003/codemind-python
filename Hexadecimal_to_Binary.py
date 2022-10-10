n=int(input())
for i in range(n):
    a=input()
    for i in a:
        if(i.isdigit()):
            k=int(i)
            k=bin(k)[2:]
            if(len(k)<4):
                s=""
                for j in range(4-len(k)):
                    s+='0'
                s+=k
                print(s,end="")
            else:
                print(k,end="")
        elif(i=='A'):
            k=10
            print(bin(k)[2:],end="")
        elif(i=='B'):
            k=11
            print(bin(k)[2:],end="")
        elif(i=='C'):
            k=12
            print(bin(k)[2:],end="")
        elif(i=='D'):
            k=13
            print(bin(k)[2:],end="")
        elif(i=='E'):
            k=14
            print(bin(k)[2:],end="")
        elif(i=='F'):
            k=15
            print(bin(k)[2:],end="")
    print()