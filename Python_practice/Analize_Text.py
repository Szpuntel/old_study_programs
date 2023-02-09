file = open ('text.txt', 'r')   #stary zapis (lepiej korzystać z openwith)
text = file.read()
file.close()

def count(txt, symbol):
    number = 0
    for s in txt:
        if s == symbol:
            number += 1
    return number

print (count(text, 'b'))    
print (count(text, 'z'))

for z in "qwertyuiopasdfghjklzxcvbnm":
    ile = count(text.lower(), z)
    procent = 100 * ile / len(text)
    print('{0} - {1} - {2}%'.format(z.upper(), ile, round(procent, 2)))