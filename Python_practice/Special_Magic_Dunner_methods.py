from numpy import full


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
        self.pay = int(self.pay * Employee.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Bob', 'Nigeroski', 11000)

print (len(emp_1))
#print(emp_1 + emp_2)


# print (int.__add__(1, 2))
# print (str.__add__('a', 'b'))

# print(emp_1)
# print(repr(emp_2))
# print(emp_1.__repr__())
# print(emp_1.__str__())
