vika = [int(x) for x in input().split()]
w = 1
while w < len(vika):
   for i in range(len(vika) - w):
       if vika[i] > vika[i + 1]:
           vika[i], vika[i + 1] = vika[i + 1], vika[i]
   w += 1
print(vika)
