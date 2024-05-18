class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        if self.name != 'Николай':
            print('Я не ' + self.name + ', а Николай' + ". Мне " + self.age)
        else:
            print ('Я '+ self.name + ". Мне " + self.age)
            
name1 = Nikola("Максим",'44')
name2 = Nikola("Николай", "25")
name3 = Nikola("Леонид Андреевич","16")

name1.show()