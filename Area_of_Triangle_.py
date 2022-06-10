x,y,z=map(int,input().split())
d=(x+y+z)/2
import math
s=math.sqrt(d*(d-x)*(d-y)*(d-z))
print("%.2f"%s)