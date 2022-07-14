x=input().split()
for i in x:
    a=[]
    for j in i:
        a.append(ord(j))
    print(max(a)-min(a),end=" ")