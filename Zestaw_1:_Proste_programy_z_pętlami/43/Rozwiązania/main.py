# ====================================================================================================>
# Zadanie 43
# Dla pewnej N-cyfrowej liczby naturalnej obliczono sumę N-tych potęg cyfr tej liczby otrzymu-
# jąc kolejną liczbę N-cyfrową. Naprzykład dla liczb :354,543,600,...suma ta wynosi 216. Niestety pierwotna
# liczba zaginęła ale wiadomo, że była to największa z możliwych takich liczb. Proszę napisać program, który
# na podstawie zachowanej sumy wyznaczy pierwotną liczbę
# ====================================================================================================>


def Zadanie_43(S):
    n = 1
    while 10**n <= S:
        n += 1
    start = 10 ** (n - 1)  # Najmniejsza liczba o n cyfrach
    end = 10**n  # Najmniejsza liczba o (n+1) cyfrach

    # Szukamy największej liczby od końca zakresu
    for liczba in range(end - 1, start - 1, -1):
        suma_poteg = 0
        tmp = liczba
        while tmp > 0:
            suma_poteg += (tmp % 10) ** n
            tmp //= 10
        if suma_poteg == S:
            return liczba
    return None


