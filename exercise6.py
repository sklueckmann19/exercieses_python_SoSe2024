a = 1
r = 0.5
s = 0
k = 0

while True:
    s += a * r**k
    k += 1
    print(s, end = "")
    if s == 2:
        break