
file = open('saved_to_file.txt', 'a')
if file.writable():
    file.write(input("Gimmie da string: ") + "\n")
file.close()

file = open('saved_to_file.txt', 'r')


if file.readable():
    for l in file:
        print (l)

# POZOSTALE SPOSOBY WYSWIETLENIA PLIKU

# if file.readable():
#     text = file.readlines()
#     for l in text:
#         print(l)

# if file.readable():
#     text = file.read()
#     print (text)