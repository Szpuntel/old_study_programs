# funkcja wyższego rzędu
    
def funkcja(f,liczba):
    return f(liczba)
# Dwie zwykłe funkcje
def dodaj_jeden(x):
    return x + 1
def kwadrat(parametr):
    return parametr*parametr
    
# Wywołanie funkcji wyższego rzędu
    
funkcja(dodaj_jeden,7) # dodaj 1
