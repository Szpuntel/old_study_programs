 # funkcja super() pozwala nam przejadz zmienne lub funkcje z classy nadrzędnej do drugiej
 # zwraca tymczasowy obiekt z klasy nadrzednej kiedy zostanie użyty np.(po to aby nie powtarzac kodu)

class Rectangle:
    def __init__(self, lenght, width):      #<----- classa z której bierzemy lenght i width
        self.width = width                  #<---- Te linie zostaną wysłane do Square i Cube 
        self.lenght = lenght                # Dzieki temu nie musimy ich ponownie pisać

class Square(Rectangle):
    def __init__(self, lenght, width):          #<----- class implementacja zmiennych
        super().__init__(lenght, width)         # <----- za pomocą super().__init__(lenght, width) 
                                                # bierzemy lenght i width z Rectangle


    def area(self):                    # <----- W funkcji nie implementujemy juz zmiennych
        return self.lenght * self.width

class Cube(Rectangle):
     def __init__(self, lenght, width, height):   #<--- To samo co powyżej tylko dodatkowo tworzymy
         super().__init__(lenght, width)          # zmienną height
         self.height = height                     # <--- implementacje height

     def volume(self):
         return self.lenght * self.width * self.height

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
