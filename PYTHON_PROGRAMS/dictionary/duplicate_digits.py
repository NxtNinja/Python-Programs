data = int(input("Enter a big number: "))
a = {}

while data != 0:
    temp = data % 10
    if temp not in a.keys():
        a[temp] = 1
    else:
        a[temp] += 1
    data //= 10

print(a)