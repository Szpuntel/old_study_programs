#Np zamiast ---- otwieranie polaczenia bazy danych i ---- zamykanie. a w srodku modyfikacje.

# Kod definiuje funkcję decorator, która jest funkcją pośrednią (ang. wrapper)
def decorator(func):
    # Funkcja wrapper wyświetla dwie linie znaków '-' przed i po wywołaniu funkcji func
    def wrapper():
        print('--------------')
        func()
        print('--------------')
    return wrapper

# Definicja funkcji hello
def hello():
    print('Hello World!')

# Użycie funkcji decorator do dekorowania funkcji hello
hello = decorator(hello)

# Wywołanie funkcji hello
hello()

# Pusta linia
print()

# Użycie dekoratora za pomocą znacznika @
@decorator
def witaj():
    print('Witaj Synu Boży')

# Wywołanie funkcji witaj
witaj()