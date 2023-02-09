def divison(x, y):
    # Ta linijka sprawdza, czy y jest różne od zera.
    # Jeśli jest równe zero, wyświetlany jest komunikat "Y == 0 !".
    assert y != 0, 'Y == 0 !'
    
    # Jeśli y jest równe zero, rzucony jest wyjątek ZeroDivisionError
    # z komunikatem "You can't divide by zero".
    if y == 0: 
        raise ZeroDivisionError("You can't divide by zero")
    
    # Jeśli y nie jest równe zero, wykonuje się dzielenie x przez y.
    print(x / y)

# Wywołanie funkcji division z argumentami 2 i 0.
# W tym przypadku y jest równe zero, więc rzucony zostanie wyjątek ZeroDivisionError.
divison(2, 0) 



def square_root(x):
    # Ta linijka sprawdza, czy x jest liczbą dodatnią.
    # Jeśli nie jest, wyświetlany jest komunikat "X < 0 !".
    assert x >= 0, 'X < 0 !'
    
    # Jeśli x jest mniejsze od zera, rzucony jest wyjątek ValueError
    # z komunikatem "Square root of negative number not defined".
    if x < 0: 
        raise ValueError("Square root of negative number not defined")
    
    # Jeśli x jest liczbą dodatnią, wykonuje się pierwiastkowanie.
    print(x ** 0.5)

# Wywołanie funkcji square_root z argumentem -2.
# W tym przypadku x jest mniejsze od zera, więc rzucony zostanie wyjątek ValueError.
square_root(-2)