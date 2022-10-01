n=int(input())
for i in range(n):
    a=input()
    k=0
    j=len(a)-1
    for l in a:
        k=k+int(l)*pow(8,j)
        j=j-1
    print(bin(k)[2:])