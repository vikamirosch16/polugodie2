import math
class Point:
    def __init__(self, x1,y1,x2,y2):
        self.x2 = x2
        self.y2 = y2
        self.x1 = x1
        self.y1 = y1
        
    def rasstoinie(self):
        a=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        print("расстояние между точками -",a)
        
    def os(self):
        if self.x1==0:
            print('точка 1 лежит на оси OY')
        if self.x2==0:
            print('точка 2 лежит на оси OY')
        if self.y1==0:
            print('точка 1 лежит на оси OX')
        if self.y2==0:
            print('точка 1 лежит на оси OX')
     
    def peremeshenie(self):
        b=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        print("модуль перемещения -",b)
          
point1 = Point(1,3,4,8)
point2 = Point(5,0,2,3)

point2.os()