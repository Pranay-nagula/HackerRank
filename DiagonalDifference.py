a = int(input())
q = 1
b = []
while q <= a:
    c = input().split()
    for j in c:
        b.append(int(j))
    q += 1
    s = 0
    for i in range(0, len(b), a+1):
        s = b[i] + s
    c = b[a-1:len(b)-(a-1)]
    d = 0 
    for i in range(0, len(c),a-1):
        d = c[i] + d
print(abs(s-d))
