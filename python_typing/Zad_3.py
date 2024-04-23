'''
3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
tekst "Liczba parzysta" / "Liczba nieparzysta"
'''

def sprawdz3parzysta(liczba: int) -> bool:
    reszta = liczba % 2
    if reszta == 0:
        return True
    else:
        return False


l1 = 7

print(f'Czy liczba {l1} jest parzysta?')
print(sprawdz3parzysta(l1))
