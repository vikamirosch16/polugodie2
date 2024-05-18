a=5
b=709 
g=[]
s=[]

for i in range(b + 1):
    if i >=a:
        g.append(i)

for i in g:
       for j in range(2, i):
           if(i % j==0):
               break;
           if(j==i-1):
              s.append(i)
print(s)
r=sum(s)
print(r)