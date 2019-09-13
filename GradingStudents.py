n = int(input())
a = [int(input()) for i in range(n)]
for i in range(len(a)):
    if a[i]>=38:
        if a[i]%5==4:
            a[i]=a[i]+1
        if a[i]%5==3:
            a[i]=a[i]+2
for i in range(len(a)):
    print(a[i])
