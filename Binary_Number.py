n=int(input())
for i in range(2**n):
    a=bin(i)
    a=a[2:]
    while(len(a)<n):
        a='0'+a
    print(a)