# ====================================================================================================>
# Zadanie 46
# Mając daną dodatnią liczbę całkowitą N , stwórzmy nową liczbę dodając kwadraty cyfr
# liczby N . Można udowodnić, że postępując w ten sposób wielokrotnie otrzymamy w końcu wynik 1 lub 4.
# Przykład:13=1^2+3^2=1+9=10(Krok1)10=1^2+0^2=1+0=1(Krok2,kończy my iterację ponieważ uzyskaliśmy liczbę 1)
# Jeżeli w opisanej powyżej procedurze uzyskamy wynik 1,to liczbę N nazywamy“jednokwadratową”.
# Proszę napisać program, który znajduje K-tą liczbę w zadanym przedziale [L, U ], która jest
# jednocześnie jedno-kwadratowa i pierwsza.
# ====================================================================================================>
# zadanie_46(0,1000000,3) -> return 3 liczba ktora spelnia wymagania w przedziale od 0 do 10000000


def jest_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def jednokwadratowa(n):
    while n != 1 and n != 4:
        suma_kwadratow = 0
        kopia = n
        while kopia > 0:
            cyfra = kopia % 10
            suma_kwadratow += cyfra**2
            kopia //= 10
        n = suma_kwadratow
    return n == 1


def Zadanie_46(L, U, K):
    znalezione = 0
    for liczba in range(L, U + 1):
        if jest_pierwsza(liczba) and jednokwadratowa(liczba):
            znalezione += 1
            if znalezione == K:
                return liczba
    return None


