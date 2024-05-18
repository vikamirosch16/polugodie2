class Bank:
    def __init__(self, people, schet, balanse):
        self.people = people
        self.schet = schet
        self.balanse = balanse
        
    def show_balanse(self):
        print ('на вашем балансе:  '+self.balanse)
    def popolnit(self):
        a=int(input('введите сумму для ввода:  '))
        b=a*0.99
        c=self.balanse + b
        print('на вашем балансе:  ',c)
    def snat(self):
        r=int(input('введите сумму для вывода:  '))
        t=r*1.01
        if self.balanse < t:
            print('на вашем счете недостаточно средств!!!')
        else:
            o=self.balanse - t
            print('на вашем балансе:  ',o)
            print('вы сняли:  ',r)
        
name1 = Bank("Максим",'1000',0)
name2 = Bank("Николай", "500",670)
name3 = Bank("Гоша","10000",8900)

name2.snat()