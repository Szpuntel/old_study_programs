sentence = input("Podaj ciag znaków: ")

def function (t):
    slowa = 1
    litery = 0
    slownik = {}
    for x in t:
        if x == ' ':
            slowa += 1
        if x != ' ':
            litery += 1
            if x in slownik:
                slownik[x] += 1
            else:
                slownik[x] = 1

    print("Liczba słów:", slowa)
    print("Liczba liter:", litery)
    print("Słownik: \n", slownik)

function(sentence) 