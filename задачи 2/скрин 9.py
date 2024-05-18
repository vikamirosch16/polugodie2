class Produkt:
    def __init__(self, name, zena, N):
        self.name = name
        self.zena = zena
        self.N = N
        
    def dobavka(self):
        print('Товара "',self.name,'" -', self.N)
        a=int(input('введите на сколько хотите увеличить количества товара:  '))
        b=self.N + a
        print('на складе теперь ',b," товар(а)")
    
    def ybrat(self):
        print('Товара "',self.name,'" -', self.N)
        a=int(input('введите на сколько хотите уменьшить количества товара:  '))
        b=self.N - a
        if a>self.N:
            print('на складе недостаточно товара для уменьшения')
        else:
            print('на складе теперь ',b," товар(а)")
    def cost(self):
        print('На складе  товара "',self.name,'" -', self.N)
        g=self.N*self.zena
        print('Общая стоимость всего товара сейчас: ',g)
        
p1 = Produkt("пончики",90,111)
p2 = Produkt("капкейки", 45,0)
p3 = Produkt("нутелла",900,30)

p1.cost()
