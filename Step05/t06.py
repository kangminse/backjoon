S=input()
a = [chr(i) for i in range(ord('a'),ord('z')+1)]
b = []
for i in range(26):
    b.append(-1)
for i in S:
    if i in a:
        b[a.index(i)] = S.index(i)

for i in b:
    print(i,end=" ")
        