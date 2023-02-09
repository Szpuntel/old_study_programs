# zabranie użytkownikowi stworzenie obiektu tej klassy
# abtract class, klasa ktora zawiera jeden lub wiecej metod
# abstract method metoda ktora jest zdeklarowana ale nie ma realizacji.

from abc import ABC, abstractmethod

class Vehicle(ABC):       # <--- Dziedziczymy ABC ktory uniemozliwa tworzenie obiektów

    @abstractmethod    # <--- dodajemy dekorator który uniemożliwa użycie tej metody
    def go(slef):      # W zasadzie mowi nam ta metoda ze jezeli chcesz jej  uzyc to musisz ja stworzyć w konkretnej klasie
        pass           # nie mozesz sobie jej odziedziczyć

    def stop(self):
        pass

class Car(Vehicle):

    def go(slef):
        print("You drive the car")

class Motorcycle(Vehicle):

    def go(slef):
        print("You ride the motorcycle")
 
car = Car()
motorcycle = Motorcycle()


car.go()
motorcycle.go()
