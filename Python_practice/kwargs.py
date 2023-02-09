# **kwargs parametr ktory zapakuje wszystkie argumenty do słownika.
# Przydatne bo funkcja moze przyjac różna liczbe argumentów 

def hello(**kwargs):  # <--- Nie musi nazywac kwargs ważne zeby nazwa zaczynała sie od '**'
   # print("Hello" + kwargs['first'] + " " + kwargs['second'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(first="Dude", middle="Bro", second="Code")

 