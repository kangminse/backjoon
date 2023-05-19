A, B = map(int, input().split())
C = int(input())

hour = A+(B+C)//60
min = (B+C)%60

if(hour>=24):
    hour-=24

print(hour, min)
    
        