h,m=map(int,input().split())

ch_m = m-45

if(ch_m < 0):
    if(h==0):
        h=23
    else:
        h-=1
    ch_m = 60+m-45
print(h, ch_m)

