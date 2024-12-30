# ====================================================================================================>
# Zadanie 57
# Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest
# liczbą pierwszą. Naprzykład: 13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo1∗3=3
# 16 jest  liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16=121(3) ,1∗2∗1=2 W liczbie naturalnej możemy
# dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092, 920. Proszę napisać funkcję, która dla
# danej liczby naturalnej N, zwróci najmniejszą podstawę systemu (z zakresu 2-16) w którym przynajmniej
# jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość None gdy taka podstawa nie istnieje.
# ====================================================================================================>


def is_prime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= x:
        if x % divisor == 0 or x % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def iloczyn_cyfr(liczba, podstawa):
    iloczyn = 1
    while liczba > 0:
        cyfra = liczba % podstawa
        liczba //= podstawa
        iloczyn *= cyfra
        if iloczyn == 0:
            break
    return iloczyn


def liczba_cyfr(liczba):
    licznik_cyfr = 0
    if liczba == 0:
        return 1
    while liczba > 0:
        liczba //= 10
        licznik_cyfr += 1
    return licznik_cyfr


def rotacja_w_lewo(liczba):
    licznik_cyfr = liczba_cyfr(liczba)
    if licznik_cyfr <= 1:
        return liczba
    potega_dziesiatki = 10 ** (licznik_cyfr - 1)
    najwazniejsza = liczba // potega_dziesiatki
    liczba %= potega_dziesiatki
    return liczba * 10 + najwazniejsza


def Zadanie_57(N):
    licznik_cyfr = liczba_cyfr(N)
    podstawa = 2
    while podstawa <= 16:
        licznik_rotacji = 0
        obrocona_liczba = N
        while licznik_rotacji < licznik_cyfr:
            if is_prime(iloczyn_cyfr(obrocona_liczba, podstawa)):
                return podstawa
            obrocona_liczba = rotacja_w_lewo(obrocona_liczba)
            licznik_rotacji += 1
        podstawa += 1
    return None


