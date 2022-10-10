n=int(input())
for i in range(n):
    a=int(input())
    a=bin(a)[2:]
    print(a.count('1'))