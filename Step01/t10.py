a=int(input())
alist=list(map(int,input()))
blist=[]

for i in alist[::-1]:
    c=a*i
    blist.append(c)
    print(c)
    
clist=[]
d=1

for i in blist:
    suma=i*d
    d*=10
    clist.append(suma)
print(sum(clist))
