class Aviakompania:
    def __init__(self,planes,marshrut):
        self.planes = planes
        self.marshrut = marshrut
        
    def append_s(self,model):
        print('вы добавили модель:',model)
        self.planes.append(model)
        print('получившийся список самолётов:',self.planes)
        
    def append_m(self,gorod):
        print('вы добавили город в маршрут:',gorod)
        self.marshrut.append(gorod)
        print('получившийся список маршрутов:',self.marshrut)
        
    def remove_s(self,model):
        print('вы удалили данную модель:',model)
        self.planes.remove(model) 
        print('получившийся список самолётов:',self.planes)

    def remove_m(self,gorod):
        print('вы удалили данный город:',gorod)
        self.marshrut.remove(gorod) 
        print('получившийся список маршрутов:',self.marshrut)    
            
    def poisk(self):
        s=[0]
        a=input('введите модель, которую хотите найти: ')
        for i in self.planes:
            if  i==a:
                print('модель есть в этом списке самолётов:',self.planes)
                s.append(1)
            else: 
                s.append(0)
        d=sum(s)
        if d==0:
             print('такая модель не найдена')
   
    def poisk2(self):
        u=[0]
        j=input('введите город, который хотите найти: ')
        for i in self.marshrut:
            if  i==j:
                print('город есть в этом маршруте:',self.marshrut)
                u.append(1)
            else: 
                u.append(0)
        d=sum(u)
        if d==0:
             print('такого города нет в маршрутах')             
             
             
b = Aviakompania(['model1','model2'],['Санкт-петербург','Астрахань','Омск'])
b.poisk2()