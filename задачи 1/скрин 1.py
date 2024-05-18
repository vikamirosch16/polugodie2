f=[]
c=[]
a='ass ddd lr rrr ly hh hh'
a=a.split()
for i in range(len(a)):
    if a[i] in f:
        c.append(a[i])
    f.append(a[i])
for i in range(len(c)):
    a.remove(c[i])
a=sorted(a)
print(a)