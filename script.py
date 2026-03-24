import random
import os
import time

class siatka:
    def __init__(self, wysokosc, szerokosc):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.mapa = []
        for i in range(wysokosc):
            row = []
            for j in range(szerokosc):
                row.append('.')
            self.mapa.append(row)



    def show(self):
        for row in self.mapa:
            print(" ".join(row))

    def change_status(self, wysokosc, szerokosc):
        self.mapa[wysokosc][szerokosc] = 'o'

    def randomize(self):
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                self.mapa[i][j] = 'o' if random.randint(0, 1) else '.'

    def _count_neighbors(self, wysokosc, szerokosc):
        count = 0
        for i in [wysokosc-1, wysokosc, wysokosc+1]:
            for j in [szerokosc-1, szerokosc, szerokosc+1]:
                if i == wysokosc and j == szerokosc:
                    continue
                if 0 <= i < self.wysokosc and 0 <= j < self.szerokosc:
                    if self.mapa[i][j] == 'o':
                        count += 1
        return count

    def next_step(self):
        new_map = []
        for i in range(self.wysokosc):
            row = []
            for j in range(self.szerokosc):
                row.append('.')
            new_map.append(row)
        for i in range(self.wysokosc):
            for j in range(self.szerokosc):
                neighbors = self._count_neighbors(i, j)
                if neighbors < 2 or neighbors > 3:
                    new_map[i][j] = '.'
                if neighbors == 3:
                    new_map[i][j] = 'o'
                if neighbors == 2:
                    new_map[i][j] = self.mapa[i][j]

        self.mapa = new_map



plansza = siatka (20,20)
plansza.randomize()

while True:
    os.system('cls')
    plansza.show()
    plansza.next_step()
    time.sleep(1)

