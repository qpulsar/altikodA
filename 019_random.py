import random

dizi = []

for i in range(0, 10):
    sayi = random.randint(1, 10)
    while sayi in dizi:
        print("aynısından buldum")
        sayi = random.randint(1, 10)
    dizi.append(sayi)


print(dizi)
