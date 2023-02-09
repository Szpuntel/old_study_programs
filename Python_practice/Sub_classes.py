class Employee:

    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language

class Menager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
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

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('John', 'Smith', 50000, 'pytong')
mgr_1 = Menager('Paulo', 'Chiki', 33000, [dev_1])
emp_2 = Employee('Bob', 'Nigeroski', 11000)



#print(issubclass(Menager, Employee))
#print(isinstance(mgr_1, Developer))
#print(isinstance(mgr_1, Menager))

# print(mgr_1.email)
# mgr_1.print_emps()
# mgr_1.add_emp(emp_2)
# mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print (dev_1.pay)
# dev_1.apply_raise()
# print (dev_1.pay)


#print(help(Developer))
# print(Developer.fullname(emp_2))
# print(Employee.fullname(emp_1))
