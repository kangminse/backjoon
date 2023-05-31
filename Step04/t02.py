N,X=map(int,input().split())
alist=[]
A=list(map(int,input().split()))

for i in A:
    if(i<X):
        alist.append(i)

for i in alist:
    print(i,end=" ")