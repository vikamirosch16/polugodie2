class Biblioteka:
    def __init__(self,spisok):
        self.spisok = spisok
        
    def show(self,book):
        self.spisok.append(book)
    def show1(self,book):
        self.spisok.remove(book) 
    def poisk(self,book):
        a=input('введите книгу, которую Вам нужно найти: ')
        for i in self.spisok:
            if  i==a:
                print('эта книга есть в списке: ',self.spisok)
                
b=Biblioteka(['Война и мир'])
b.show("Klassik")
print(b.spisok)