a = input().split()
l = []
p = []
for i in a:
    l.append(int(i))
q = 0
while q < len(l):
    p.append(sum(l)-l[q])
    q += 1
print(min(p),max(p))
