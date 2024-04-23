# Zad. 2. Dla osób posiadających podstawową wiedzę o pythonie:
'''
b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
zwróci. Zadanie należy wykonać w 2 wersjach:
i. Wykorzystując pętle for .
ii. Wykorzystując listę składaną.
'''

print("Zadanie 2b. ppkt.i")
# wersja i.

lista = [2,5,8,13,22]

print("Lista pierwotna")
for i in range(len(lista)):
    print(lista[i])

def pomnoz_przez_2(lista_liczb):
    for i in range(len(lista_liczb)):
        lista_liczb[i] = lista_liczb[i] * 2
    return lista_liczb

lista2 = pomnoz_przez_2(lista)

print("Lista pomnożona przez 2")
for i in range(len(lista2)):
    print(lista2[i])

# wersja ii.
print("Zadanie 2b. pkt. ii")

lista = [1,2,3,4,5]

print("Lista pierwotna")
for i in range(len(lista)):
    print(lista[i])

def pomnoz_przez_2v2(lista_liczb):
    lista_liczb2 = [x*2 for x in lista_liczb]
    return lista_liczb2


print("Lista pomnożona przez 2 v2")
lista2 = pomnoz_przez_2v2(lista)
for i in range(len(lista2)):
    print(lista2[i])
