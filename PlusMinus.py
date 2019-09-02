a = int(input())
b = input().split()
l = []
p =[]
q=[]
w=[]

if a == len(b):
    for i in b:
        l.append(int(i))
    for j in l:
        if j<0:
            p.append(j)
        elif j>0:
            q.append(j)
        else:
            w.append(j)
    lesszero = len(p)/a
    greaterzero = len(q)/a
    equal = len(w)/a
print(greaterzero)
print(lesszero)
print(equal)
