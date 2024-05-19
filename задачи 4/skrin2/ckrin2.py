inp = open('bbb.txt','r')
q = [x for x in inp.readline().split()]
m=[]
for i in range(len(q)):
   a=q.count(q[i])
   m.append(i)
print(q[max(m)])
   
