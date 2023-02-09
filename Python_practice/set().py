#"Set" to rodzaj kolekcji danych w języku Python, która przechowuje unikalne wartości.
# Aby utworzyć zbiór, można użyć funkcji set() i przekazać do niej listę elementów. Przykład:


def scramble(s1, s2):
    set_s1 = set()
    set_s2 = set()
    for l in s1:
        set_s1.add(l)
    for l in s2:
        set_s2.add(l)

    print(set_s1, set_s2)
    return set_s1, set_s2

scramble('sdadasdsadweweqr','dasgdasderegger')