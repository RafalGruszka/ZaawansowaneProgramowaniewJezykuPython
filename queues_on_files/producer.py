'''
2. Uruchomienie producera ma skutkować zapisem do pliku 1 rekordu
odpowiadającego 1 pracy (np. 1 rozmowie telefonicznej).
'''

from datetime import datetime, date

with open('queue.txt', 'a') as f:
    f.write('zadanie' + ' ' + str(datetime.now()) + ' pending' + '\n')
