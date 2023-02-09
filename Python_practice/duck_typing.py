from faulthandler import dump_traceback
from this import s
# Duck typing    " IF IT WALKS LIKE A DUCK AND IT QUACKS LIKE A DUCK THEN IT MUST BE A DUCK "
# Jest to koncepcja powiazana z dynamicznym typowaniem, gdzie typ lub klasa obiektu 
# są mniej istotne niż metoda lub inny składnik ktore definują.
# Nie sprawdza typu zamiast tego sprawdza obecnosc metody lub innego składnika

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f'To je {self.name}'

class Product:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def info(self):
        return f'To je {self.name} i masz jego {self.quantity} sztuk.'

class Greeting:

    @staticmethod
    def greeting(person):        # <-- deafultowo ustawiamy sobie person, ale metoda wykona sie rownież dla
        print('Hello')           # innej klasy ale tylko jeżeli to inna klasa bedzie istnieć
        print(person.info())     # <------  również posiadała tą metode .info()





person_1 = Person("Rafael")
product_1 = Product("Mleko", 10)

Greeting.greeting(person_1)
Greeting.greeting(product_1)