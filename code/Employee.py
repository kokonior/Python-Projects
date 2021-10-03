class Employee:
    #classvariable
    raise_amount = 1.05
    num_employee = 0
    
    def __init__(self, name, email, pay):
        self.name = name
        self.email = email + '@company.com'
        self.pay = pay
        
        Employee.num_employee += 1
        
    def showInfo(self):
        return '{} {}'.format(self.name, self.email)
        #return print(f'Nama: {self.name}, email: {self.email}, pay: {self.pay}')
    
    def apply_raise(self):
        self.pay = int(self.pay*Employee.raise_amount )

#print(Employee.num_employee)
        
em1 = Employee('Sabrina Nurul N','sabrinanuruln', 50000)
em2 = Employee('Rizky Andhika A','rizkyandikaakbar', 100000)

#print(Employee.num_employee)
#em1.showInfo()
#em2.showInfo()
print(em1.pay)
em1.apply_raise()
print(em1.pay)
