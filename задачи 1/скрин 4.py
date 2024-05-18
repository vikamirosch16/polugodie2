import random
b=random.randint(1,3)
if b==3:
    b='бумага'
if b==1:
    b='камень'
if b==2:
    b='ножницы'
a=input('ваш ход: ')
print("бот выбрал: ",b)
if a==b:
    print('у вас ничья')
else:
    if a=='Бумага':
        if b=='Камень':
            print('Вы выиграли')
        else:
            print('вы проиграли')
    if a=='Камень':
        if b=='Бумага':
            print('вы проиграли')
        else:
            print('вы выиграли')
    if a=='Ножницы':
        if b=='Бумага':
            print('вы выиграли')
        else:
            print('вы проиграли')