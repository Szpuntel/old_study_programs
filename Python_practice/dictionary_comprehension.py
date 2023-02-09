 # dictionary = {key: expression for (key,value) in iterable}
#  Słownik = {klucz: wartość wyrażenia dla (klucz, wartość) w iterowalnym obiekcie}


# Tworzenie słownika na podstawie innego słownika - przykład z temperaturami w stopniach Farenheita
cities_in_f = {'New York': 32, 'Boston': 64, 'Los Angeles': 100, 'Czikago': 50}

# Konwersja temperatur z stopni Farenheita na stopnie Celsjusza
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_f.items()}

# Wypisanie nowego słownika z temperaturami w C
print(cities_in_C)

# -----------------------------

# Przykład z if - tworzenie słownika z pogodą w miejscach
weather = {'Poland': 'sunny', 'Germany': 'sunny', 'Italy': 'sunny', 'France': 'cloudy'}

# Tworzenie słownika z miejscami, które są słoneczne
sunny_weather = {key: value for (key,value) in weather.items() if value == 'sunny'}

# Wypisanie słownika z miejscami z słoneczną pogodą
print(sunny_weather)

# -----------------------------

# Przykład z if else - tworzenie słownika z określeniem czy temperatura jest ciepła czy zimna
cities = {'New York': 32, 'Boston': 64, 'Los Angeles': 100, 'Czikago': 50}

# Tworzenie słownika z określeniem czy temperatura jest ciepła czy zimna
warm_or_cold = {key: ("WARM" if value >50 else "COLD") for (key,value) in cities.items()}

# Wypisanie słownika z określeniem ciepła/zimna
print(warm_or_cold)

# -----------------------------

# Przykład z funkcją - tworzenie słownika z opisem temperatury (ciepła/zimna)
def check_temp(value):
    if value > 55:
        return "HOT"
    else:
        return "COLD"

cities = {'New York': 32, 'Boston': 64, 'Los Angeles': 100, 'Czikago': 50}

# Tworzenie słownika z opisem temperatury (ciepła/zimna)
desc_cities ={key: check_temp(value) for (key,value) in cities.items()}

# Wypisanie słownika z opisem temperatury (ciepła/zimna)
print(desc_cities)