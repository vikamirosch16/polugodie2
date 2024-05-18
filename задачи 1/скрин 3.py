a='а лес у села'
for i in range(len(a)):
    a=a.replace(' ','')
    a=a.replace('.','')
    a=a.replace('!','')
    a=a.replace(',','')
b=a[::-1]
if b==a:
    print('Полиндром')