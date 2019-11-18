a = input('Vedite cifru: ').split()

w = []
for i in a:
    w.append(int(i))

b = []
c = []
for s in w:
    if s % 2 == 0:
        b.append(s)
    elif s % 2 != 0:
        c.append(s)
    else:
        None
print(b)
print(c)
