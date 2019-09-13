a = input("")
if a[-2:] == "AM":
    if a[:2] == "12":
        print("00"+a[2:8])
    else:
        print(a[0:8])
elif a[-2:] == "PM":
    b = str(int(a[:2]) + 12)
    if b == "24":
        b = "12"
        print(b+a[2:8])
    else:
        print(b+a[2:8])
