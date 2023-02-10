import csv

class Item:
    pay_rate = 0.8 # 20% zniżka 
    all = []
    def __init__(self, name: str, price: float, quantity=0):

        # Walidacja danych
        assert price > 0, "Cena musi być większa od zera. "
        assert quantity >= 0, "Ilość nie może być ujemna. "

        # Pzypisanie atrybutyów do instancji

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long")
        else:
            self.__name = value

        # Zapisanie każdego utworzonego obiektu  do listy all


        # Zwraca nazwe obiektu jak chcemy zamiast wskazywać na zajmowane miejsce w pamieci.

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"

    def apply_discount(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):   # W Metodach clasy odwołujemy sie do classy wiec zawsze musi być cls aby móc wywołać metode na klasie
        with open('praktyka\oop_practice\oop_practice_items.csv') as f:          # np. Item.instantiate_from_csv() ---> nazwaklasy.metoda()
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):     # <-- Sprawdza czy dana zmienna jest floatem
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
