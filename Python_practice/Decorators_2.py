# Kod definiuje funkcję decoratora start_end_decorator
def start_end_decorator(func):
    # Funkcja wrapper wyświetla dwie linie znaków '~' przed i po wywołaniu funkcji func
    def wrapper(*args, **kwargs):
        print ("~~~~~~~~")
        func(*args, **kwargs)
        print ("~~~~~~~~")
    return wrapper

# Użycie dekoratora za pomocą znacznika @
@start_end_decorator
def print_name():
    print ('Rafael')

# Użycie dekoratora za pomocą znacznika @
@start_end_decorator
def add5(x):
    print( x + 5 )

# Wywołanie funkcji add5 z argumentem 10
add5(10)

# Wywołanie funkcji print_name
print_name()


'''*args i **kwargs są specjalnymi składnikami składni języka Python, które umożliwiają przekazywanie nieznanej liczby argumentów do funkcji.

*args jest używane, gdy chcesz przekazać nieznane liczby argumentów do funkcji jako tuple (krotka).

**kwargs jest używane, gdy chcesz przekazać nieznane liczby argumentów do funkcji jako słownik (dictionary).

W powyższym kodzie, argumenty nieznanej liczby zostaną przekazane do funkcji wrapper za pomocą *args i **kwargs,

 co umożliwia wywołanie funkcji func z tymi samymi argumentami.'''