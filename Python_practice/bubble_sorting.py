
ile = input("Ile elementów chcesz wprowadzic do listy: ")
10
tyle = int(ile)
lista = []
while int(tyle) != 0:
    miejsce = 0
    print(f"wprowadz {miejsce+1} element: ") 
    lista.insert(miejsce,input())
    tyle -= 1
    miejsce += 1


def sortowanieBombelkowe(lista):
    n = len(lista)
    zamien = False
    while n > 1:

        for l in range(0, len(lista)-1):
            if lista[l]%2 !=0 and lista[l+1]%2 !=0:
                if lista[l] > lista [l+1]:
                    lista[l], lista[l+1] = lista [l+1], lista[l]
                    zamien = True

        n -= 1
        if zamien == False: break

    return lista

sortowanieBombelkowe(lista)

print(lista)
