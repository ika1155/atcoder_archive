s=str(input().rstrip())
moji=[]


for i in range(len(s)): #できる単語の数
    if i == 0:
        moji.append(s)
    else:
        a=""
        a += s[i:]
        a += s[:i]
        moji.append(a)

min=moji[0]
max=moji[0]

for i in range(1, len(s)):
    t=moji[i]
    
    if min>t:
        min=t
    elif max<t:
        max=t
    else:
        continue

print(min)
print(max)