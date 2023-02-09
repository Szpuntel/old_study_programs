countries_information = {}
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)

def show_country_info(country):
    country_information = countries_information.get(country)

    print()
    print(country)
    print("----------")
    print("Stolica: " + country_information[0])
    print("Liczba mieszkancow: " + str(country_information[1]) + " Milionów")

for country in countries_information.keys():
    print (country)

country = input("o jakim kraju chcesz info ? ")
show_country_info(country)
