s, t, x = map(int, input().split())
ans = "No"
if s < t:
    if s <= x < t:
        ans ="Yes"
else:
    if s <= x <=23 or 0 <= x < t:
        ans ="Yes"




print(ans)
