class Krik:
    def __init__(self, dobavka):
        self.dobavka = dobavka 
        
    def show(self):
        if self.dobavka == '':
            print('Обычная газировка')
        else:
            print ('газировка', self.dobavka)
            
krik1 = Krik("dobavka1")
krik2 = Krik("dobavka2")
krik3 = Krik("")

krik2.show()
