# Klasa bazowa "Animal"
class Animal:
    # Konstruktor z parametrami "name" i "age"
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Klasa pochodna "Dog" dziedzicząca z "Animal"
class Dog(Animal):
    # Metoda zwracająca dźwięk psa
    def voice(self):
        print("How how ")

# Klasa pochodna "Wolf" dziedzicząca z "Dog"
class Wolf(Dog):
    # Metoda zwracająca dźwięk wilka i dźwięk psa
    def getVoice(self):
        print("I am a wolf xd")
        super().voice()
    
# Klasa pochodna "Cat" dziedzicząca z "Animal"
class Cat(Animal):
    # Metoda zwracająca dźwięk kota
    def getVoice(self):
        print('Meow meow')

# Tworzenie obiektu "cat" z klasy "Cat"
cat = Cat('Mia', 2)
# Tworzenie obiektu "dog" z klasy "Dog"
dog = Dog('Reksio', 4)
# Tworzenie obiektu "wolf" z klasy "Wolf"
wolf = Wolf('Patyk', 3)

# Wywoływanie metody "getVoice" dla obiektu "cat"
cat.getVoice()
# Wywoływanie metody "voice" dla obiektu "dog"
dog.voice()
# Wyświetlanie nazwy obiektu "dog"
print(dog.name)
# Wywoływanie metody "voice" dla obiektu "wolf"
wolf.voice()