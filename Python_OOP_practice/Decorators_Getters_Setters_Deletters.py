"""
Gettery, settery i deletery to specjalne dekoratory (ang. decorators), które pozwalają na odpowiednie udekorowanie metod w klasach w Pythonie.

Gettery (ang. getters) są to metody oznaczone jako @property, które udostępniają wartość właściwości (ang. property) klasy.
Wartość ta jest odczytywana jak zmienna, ale faktycznie jest to wartość zwrócona przez metodę.

Settery (ang. setters) są to metody oznaczone jako @nazwa_właściwości.setter,
które pozwalają na ustawienie wartości właściwości klasy.

Deletery (ang. deleters) są to metody oznaczone jako @nazwa_właściwości.deleter,
które pozwalają na usunięcie wartości właściwości klasy. W ich przypadku, po wywołaniu del na daną właściwość, wywoływana jest metoda deletera.
"""

# Tworzenie klasy Employee
class Employee:
    
    # Inicjalizator klasy, wywoływany przy tworzeniu obiektu
    def __init__(self, first, last, pay):
        # Atrybuty obiektu
        self.first = first
        self.last = last
        self.pay = pay

    # Dekorator @property, oznacza że ta funkcja jest właściwością (getterem)
    @property
    def email(self): 
        # Zwraca adres email w postaci "first.last@email.com"
        return '{}.{}@email.com'.format(self.first, self.last)
    
    # Dekorator @property, oznacza że ta funkcja jest właściwością (getterem)
    @property
    def fullname(self):
        # Zwraca pełne imię i nazwisko w postaci "first last"
        return '{} {}'.format(self.first, self.last)

    # Dekorator @fullname.setter, oznacza że ta funkcja jest setterem dla właściwości fullname
    @fullname.setter
    def fullname(self, name):
        # Dzieli pełne imię i nazwisko na dwie części i ustawia jako first i last
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Dekorator @fullname.deleter, oznacza że ta funkcja jest deleterem dla właściwości fullname
    @fullname.deleter
    def fullname(self):
        # Wypisuje komunikat "Delete Name!" i ustawia first i last na None
        print ('Delete Name!')
        self.first = None
        self.last = None

# Tworzenie obiektu Employee
emp_1 = Employee('John', 'Smith', 50000)

# Zmiana wartości atrybutu first na Jimmy
emp_1.first = 'Jimmy'

# Zmiana wartości właściwości fullname
emp_1.fullname = 'Bobbili Smidfdth'

# Wypisywanie wartości atrybutów first, email, fullname
print (emp_1.first)
print (emp_1.email)  
print (emp_1.fullname)

# Usuwanie właściwości fullname
del emp_1.fullname

# Wypisywanie wartości atrybutów first, email, fullname
print (emp_1.first)
print (emp_1.email)  
print (emp_1.fullname)
