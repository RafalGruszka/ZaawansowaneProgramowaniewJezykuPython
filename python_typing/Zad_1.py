'''
1. Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie
go wyświetlić ( print )
'''

def powitanie (name: str, surname: str)  -> str:
    return f'Cześć {name} {surname}!'

powit = powitanie('Rafał', 'Gruszka')
print(powit)
