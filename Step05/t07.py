T=int(input())

for i in range(T):
    R,S = map(str,input().split())
    result = ""
    for j in S:
        result+=(j*int(R))
    print(result)


