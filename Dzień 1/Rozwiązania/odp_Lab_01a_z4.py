"""
Lista 01a Zadanie 4
"""
# czysci ekran
from os import system
system('cls')

x = float(input("Podaj wartość ? "))  # wczytuję dane i zamieniam na float

# przeliczam na lbs
lbs = x * 2.2
# przeliczam na kg
kg = x * 0.45

# wypisuje na ekran  f - string formatowanie wyjscia
print(f"{x} kg to {lbs:0.1f} lbs")
print(f"{x} lbs to {kg:0.1f} kg")
# zatrzymuję działanie programu
input()
