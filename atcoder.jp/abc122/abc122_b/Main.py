s=input()
count=[0]
c=0
ac=["A", "C", "G", "T"]


for i in range(len(s)):
    if s[i] in ac:
        c += 1
    else:
        count.append(c)
        c=0
count.append(c)

print(max(count))