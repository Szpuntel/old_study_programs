class Human:                                                                # Klasa

    def __init__(self,name,age):                                            # Konstruktor
        self.name = name
        self.age = age

    def introduce_yourself(self, greetings = "Whats up !"):                 # funkcja/metoda
        return greetings +" My name is " + self.name \
               + "and im "+ str(self.age) +" years old"

person = Human('Anderw', 54)                                                # Obiekt
person2 = Human('Bobby', 24)
person2.name = 'John'

print(person.name)
print(person.introduce_yourself())
print(person2.name)
