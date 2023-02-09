# zip = łączy wartosci z dwóch lub wiecej listy/krotki i tworzy nową posiadajaca wszystkie te wartosci.

# ERRORRR ValueError: too many values to unpack (expected 2) oznacza ze prawdopodobnie zapomniałeś dodać .items() do słowika !

username = ['Dude', 'Admin', 'Potat'] # <-- LISTA
passwords = ('cooldude123', 'admin123', 'ihavepotatobloodinmyveins') # <-- KROTKA
login_date = ['1/1/2001', '26/04/2005', '5/7/2004']

# username_passwords = zip(username, passwords)  # <---  Zostawiamy jako typ ZIP

username_passwords = list(zip(username, passwords, login_date)) # <---- Konwersja na Liste

#username_passwords = dict(zip(username, passwords, login_date))   # <---- Konwersja na Słownik

# for key,value in username_passwords.items():          
#     print(key + ' : ' + value)


for i in username_passwords:
    print(i)