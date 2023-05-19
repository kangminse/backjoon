alist=list(map(int,input().split()))

blist=[]
cnt=0
eql=0
for i in alist:
    if(i in blist):
        cnt+=1
        eql=i
    else:
        blist.append(i)

if(cnt==2):
    print(10000+eql*1000)
elif(cnt==1):
    print(1000+eql*100)
elif(cnt==0):
    print(max(blist)*100)



