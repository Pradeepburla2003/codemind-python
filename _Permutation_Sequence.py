from itertools import permutations as pp
a,b=map(int,input().split())
x=''.join([str(i) for i in range(1,a+1)])
a=list(pp(x,len(x)))
print(''.join(a[b-1]))