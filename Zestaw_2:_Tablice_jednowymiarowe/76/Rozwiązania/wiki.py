# ====================================================================================================>
# Zadanie 76
# Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w
# obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
# (z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
# sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+4+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
# i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
# tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.
# ====================================================================================================>
# return liczba znalezionych sum  dajacych liczbe pierwsza


from math import sqrt

# maska tritowa :))
# 0 - element z tablicy 1, 1 - element z tablicy 2, 2 - elementy z obu tablic
# system trójkowy: n % 3: [ 0, 1, 2 ]


def czy_pierwsza(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i < sqrt(n + 1) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end while
    return True


def mask_creation(t1, t2, mask):
    suma = 0

    for i in range(len(t1)):
        if mask % 3 == 0:
            suma += t1[i]
        elif mask % 3 == 1:
            suma += t2[i]
        elif mask % 3 == 2:
            suma += t1[i] + t2[i]
        mask //= 3
    return suma


def maska_tritowa(t1, t2):
    licznik = 0
    for mask in range(3 ** len(t1)):
        if czy_pierwsza(mask_creation(t1, t2, mask)):
            licznik += 1
    # end for
    return licznik


