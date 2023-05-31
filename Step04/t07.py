alist=[i for i in range(1,31)]

for i in range(28):
    n=int(input())
    alist.remove(n)
    
sorted(alist)
print(alist[0])
print(alist[1])
