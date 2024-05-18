class triangleChecker:
    def __init__(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c
        
    def is_triangle(self):
        if type(self.a)==int and type(self.b)==int and type(self.c)==int:
            if self.a > 0 and self.b > 0 and self.c > 0:
                if self.a+self.b > self.c and self.a+self.c > self.b and self.c+self.b > self.a:
                    print('ура можно построить треугольник!')
                else:
                    print('нельзя построить')
            else: 
                print('с отрицательными числами ничего не выйдет! ')
        else:
            print('нужно вводить только числа')
            
tre1 = triangleChecker(1,2,3)
tre2 = triangleChecker(2,2,2)
tre3 = triangleChecker('u', 'v', 2)
tre4 = triangleChecker(-3, 4, 5)

tre4.is_triangle()