n='256 9'
d = n.split()
a=int(d[0])
b=int(d[1])
c=b//2
L=[]
while(a>0):
    L.append(a%2)
    a=a//2
L.reverse()
h=len(L)
v=b-h
if h <= b:
    for i in ra nge(v):
        L.insert(i,0)
    for j in L:
        print(j,end='')
    # print(L)
else:
    print("-1")
