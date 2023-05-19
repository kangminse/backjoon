'''
Created on 2023. 5. 18.

@author: user
'''
from collections import Counter
N=int(input())
alist=list(map(int,input().split()))
v=int(input())
cnt=Counter(alist)

print(cnt[v])

