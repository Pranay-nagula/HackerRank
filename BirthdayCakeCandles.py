a = int(input())
b = list(map(int, input().split()))
c = (max(b))
d = []
for i in range(len(b)):
    if c == b[i]:
        d.append(b[i])
print(len(d))
