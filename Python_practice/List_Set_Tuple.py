# name_list = []
# name_list.append("Kamil")
# name_list.append("Mariusz")

# for name in name_list:
#     name_list.sort()
#     print(name)

# name_list = ['kamil','andrzej','adam']

# name_list2 = ['dominik']

# name_list3 = name_list + name_list2

# name_list3.sort(reverse=True)
# print(name_list3)


# name = [aaa] == LISTA
# name = (aaa) == KROTKA (NIE MOZNA MODYFIKOWAC)
# name = {aaa} == SET  NIE MOZNA MIEC ZDUPLIKOWANYCH DANYCH / nie sa uporzadkowae

# person = ("Kamil", "Dupinski", 32)
# print (person.count("Kamil"))

# names_set = set()
# names_set.add("kamil")
# names_set.discard("Adolf")

# names_set = {"Kamil", "Mariusz", "Kamil"}
# names_set2 = ["koko"]

# print(names_set2)

# names_set3 = names_set.union(names_set2)

# print(names_set3)

# names_set.difference (names_set2)

countries_and_capitals = {"Poland":"Warsaw","Germany":"Berlin"}

print (countries_and_capitals)

countries_and_capitals['Czechia'] = "Prague"

for country, capital in countries_and_capitals.items():
    print(country +"_"+ capital)

print (countries_and_capitals.get["Poland"])
