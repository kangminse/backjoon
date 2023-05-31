result=0
cnt=0
for i in range(9):
    a=int(input())
    if(result<a):
        result=a
        cnt=i
print(result)
print(cnt+1)