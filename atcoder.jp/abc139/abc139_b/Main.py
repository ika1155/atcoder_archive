a, b=map(int,input().split())

c=1
t=0

while c<b:
    t += 1
    c = c - 1 + a

print(t)