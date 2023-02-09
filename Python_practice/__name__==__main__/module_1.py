# moduł moze zostać uruchomiony przez odzielny program
# moduł moze zostać zaimportowany i uzyty przez inne moduły

# iterpreter pythona ustawia "specjalne zmienne" jedna z nich jest __name__
# i python przypisze zmiennej __name__ wartość z __main__ jeżeli początkowy moduł zostanie uruchomiony

# w skrócie przy importowaniu drugiego pliku,  ten drugi plik sie wykonuje bez wzgledu czy tego chcemy czy nie
# wykorzystująć if __name__ == "__main__": sprawiamy ze plik sie nie wykona za prosrednictwem importa lecz tylko
# wtedy kiedy go wywołamy ' module_1.hello() '


def hello():
    print('HOLLA AMIGO !')


if __name__ == "__main__":
    hello()