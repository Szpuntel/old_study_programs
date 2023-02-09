lista = []
lista_u = []
x = 1
while True:
    x = input("Podej liczbe ")
    if int(x) == 0: break
    lista.append(x)
    print("dodano !")


for i in lista:
    if i not in lista_u:
        lista_u.append(i)

print(lista)
print(sorted(lista_u))        