class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'
        Employee.num_of_emps += 1
        

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    
    @staticmethod #Nie uzywa zadnej zmiennej z clasy wiec robimy staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True




emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Bob', 'Nigeroski', 11000)





# import datetime
# my_date = datetime.date(2016, 7, 10)
# print(Employee.is_work_day(my_date))

# emp_str_1 = 'Jimmy-Doe-76055'
# emp_str_2 = 'Dimitrov-Spiritov-23044'

# emp_3 = Employee.from_string(emp_str_1)

# print(emp_3.email)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

#print(Employee.num_of_emps)
# print (emp_1.__dict__)

# emp_1.raise_amount = 1.05

# print (emp_1.__dict__)

# print (emp_1.pay)
# emp_1.apply_raise()
# print (emp_1.pay)


# print(emp_1.email)
# print(emp_2.fullname())
# print(Employee.fullname(emp_1))


# emp_1.first = 'John'
# emp_1.last = 'Smith'
# emp_1.email = 'john.smith@example.com'
# emp_1.pay = 50000

# emp_2.first = 'Bob'
# emp_2.last = 'Nigeroski'
# emp_2.email = 'Bob.Nigeroski@example.com'
# emp_2.pay = 11000