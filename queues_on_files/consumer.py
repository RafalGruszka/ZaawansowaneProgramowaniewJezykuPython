'''
Zadanie do wykonania - kolejkowanie rozmów na
plikach, wymagania:
1. Należy stworzyć 2 pliki uruchomieniowe:
a. producer.py - plik odpowiedzialny za zapisywanie do pliku (txt lub csv)
pracy do wykonania.
b. consumer.py - plik odpowiedzialny za wykonywanie zapisanej pracy.
2. Uruchomienie producera ma skutkować zapisem do pliku 1 rekordu
odpowiadającego 1 pracy (np. 1 rozmowie telefonicznej).
3. Wykonanie każdej pracy trwa 30s.
4. Consumer ma byś stale uruchomiony (while true) i co np. 5s odczytywać plik i
sprawdzać czy nie ma jakiejś pracy do wykonania.
5. Jeśli Consumer napotka w pliku pracę do wykonania to ją “Konsumuje” i
zaczyna ją wykonywać, po uprzedniej zmianie statusu pracy.
6. W pliku każda praca ma mieć określony status z 3 możliwych:
a. pending - praca czeka na consumera (takiego operatora), praca z takim
statusem jest zapisywana przez producera.
b. in_progress - praca została pobrana/skonsumowana przez konsumera.
c. done - praca została wykonana przez konsumera.

Zadanie ma zostać umieszczone na branchu queues_on_files
'''

import time
task = None     # Zadanie do wykonania

while True:
    time.sleep(5)
    print('Sprawdzam czy jest zadanie do wykonania...')

    # Pobranie zadanie (zmiana statusu zadania z "pending" na "in progress")
    f = open('queue.txt', 'r')
    lines = f.readlines()
    x = len(lines)

    for i in range(x):
        if lines[i].find('pending') > 0:
            lines[i] = lines[i].replace('pending', 'in progress')
            task = lines[i]
            break
    f.close()

    f = open('queue.txt', 'w')
    f.writelines(lines)
    f.close()

    # Wykonanie zadania (30s)
    if task is not None:
        try:
            print(task)
            print('Start... Czas wykonania zadania: 30s.')

            for i in range(30):
                print('*', end="")
                time.sleep(1)
            print('\n')
            #y = 1/0  # Symulacja błędu
            print('Zadanie wykonane!')
        except Exception as error:
            print(error)
            print('Błąd! Zadanie nie zostało wykonane!')
            task = None
            continue

        # Zmiana statusu zadania na "done" tylko jeśli zadanie zostało wykonane
        f = open('queue.txt', 'r')
        lines = f.readlines()
        x = len(lines)

        for i in range(x):
            if lines[i] == task:
                lines[i] = lines[i].replace('in progress', 'done')
                break
        f.close()

        f = open('queue.txt', 'w')
        f.writelines(lines)
        f.close()
        task = None

