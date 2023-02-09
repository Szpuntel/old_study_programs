pier = input("1st sentence: ")
drug = input("2nd sentence: ")

pier_lista = pier.split(" ")
drug_lista = drug.split(" ")

for x in pier_lista:
    o = 0
    if x == drug_lista[o]:
        print("Common part is", x)
        o += 1
    