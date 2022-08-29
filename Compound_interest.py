p,r,t=map(int,input().split())
c=(p*(1+r/100)**t)
c="{:.2f}".format(c)
print(c)