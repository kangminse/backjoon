alist=[]
for i in range(10):
    n=int(input())
    cal=n%42
    alist.append(cal)
blist = set(alist)
print(len(blist))
