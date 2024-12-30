# ====================================================================================================>
# Zadanie 58
# Proszę napisać program znajdujący jak najwięcej liczb N-cyfrowych dla których suma N-
# tych potęg cyfr liczby jest równa tej liczbie, np. 153=13+53+33.
# ====================================================================================================>
# testy obejmuja liczby od 1 do 9 cyfrowych włącznie.

N = 9


def suma_poteg_cyfr(liczba, n):
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10
        suma += cyfra**n
        liczba //= 10
    return suma


def Zadanie_58():
    for n in range(1, N + 1):
        for liczba in range(10 ** (n - 1), 10**n):
            if liczba == suma_poteg_cyfr(liczba, n):
                print(liczba)
