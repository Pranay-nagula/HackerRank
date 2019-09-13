a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))
f, p, l, m = [], [], [], []
for i in d:
    f.append(i+b[0])
for j in e:
    p.append(j+b[1])
for u in range(len(f)):
    if f[u] in range(a[0],a[1]+1):
        l.append(f[u])
for o in range(len(p)):
    if p[o] in range(a[0],a[1]+1):
        m.append(p[o])
print(len(l))
print(len(m))
