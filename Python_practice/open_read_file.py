
try:
    with open('test.txt') as file:     #<--- Otwieramy plik
       print(file.read())

except FileNotFoundError:
    print("File not found")

text = "Yoooooooo \nDas some more text"

with open('test.txt', 'a') as file: # <-- 'a' < -- dodaje do pliku 
    file.write(text)

 