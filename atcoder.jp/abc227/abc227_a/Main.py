n,k,a=map(int,input().split())

#何周か配る場合
if n <= k:
    k = k%n
    if k == 0:
        k = n

m = a + k -1

if m > n:
    s = (m) % n
elif m == n:
    s = n
else:
    s = m

print(s)