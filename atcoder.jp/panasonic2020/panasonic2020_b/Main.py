#https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b

h, w=map(int,input().split())

s= h*w
if h == 1 or w == 1:
    print(1)
elif s%2 == 0:
    print(int(s/2))
else:
    print(int(s/2)+1)