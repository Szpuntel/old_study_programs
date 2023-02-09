b = [1, 3, 4, 6, 7, 10]
st = "Python tutorial"
sliceportion = slice(0, 4)
print(b[sliceportion])
print(st[sliceportion])

print(st[0:15]) #<-- pierwsza wartość oznacza poczatek string, druga jego koniec jeżeli niema wartości to 
print(st[::-1])     # domyślna wartościa jest początek i koniec stringa, 3cia wartość moze posłużyc do odwracanie stringa