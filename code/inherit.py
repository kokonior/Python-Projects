class Employee:
    #classvariable
    raise_amount = 1.05
    
    def __init__(self, name, email, pay):
        self.name = name
        self.email = email + '@company.com'
        self.pay = pay
        
    def showInfo(self):
        return '{} {}'.format(self.name, self.email)
        #return print(f'Nama: {self.name}, email: {self.email}, pay: {self.pay}')
    
    def apply_raise(self):
        self.pay = int(self.pay*Employee.raise_amount)

class Developer(Employee):
    raise_amount = 1.5
        
    def __init__(self, name, email, pay, rule):
        super().__init__(name, email, pay)
        self.rule = rule
                
class Manager(Employee):
    def __init__(self, name, email, pay, employees=None):
        super().__init__(name, email, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.name)
            
dev1 = Developer('Rizky Andhika Akbar','rizkyandikaakbar', 100000, 'Software Engineer')

mng1 = Manager('Andreas', 'andreashinot', '60000', [dev1])
#print(mng1.email)
#mng1.add_emp(dev2)
#mng1.add_emp(dev3)
#mng1.remove_emp(dev2)
#mng1.remove_emp(dev3)
#mng1.print_emp()
