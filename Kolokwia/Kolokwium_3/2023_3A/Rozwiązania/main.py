# ====================================================================================================>
# Zadanie 3A, 2024-01-18
# Dany jest ciąg 𝑁 liczb naturalnych, z których wybieramy spójny fragment o długości 𝐾 (1 < 𝐾 < 𝑁).
# Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania albo
# mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić
# dwa jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który
# pozwala zbudować wyrażenie o wartości będącej liczbą pierwszą, taką że stosunek tej liczby pierwszej
# do długości znalezionego fragmentu jest największy. Proszę napisać funkcję find_max(T), która dla
# ciągu zawartego w tablicy T, wyznaczy wartość maksymalnego ilorazu jaki można znaleźć. Jeżeli taki
# podciąg nie istnieje funkcja powinna zwrócić wartość zero.
# Na przykład dla ciągu: 7, 8, 6, 4, 7, 3 funkcja powinna zwrócić wartość 16.6.
# Możliwe podciągi dające liczby pierwsze to:
# 7 + 8 ⋅ 6 + 4 = 59, 59/4 = 14.75
# 7 + 8 ⋅ 6 + 4 ∗ 7 = 83, 83/5 = 16.6
# 6 ⋅ 4 + 7 = 31, 31/3 = 10.(3)
# 4 + 7 = 11, 11/2 = 5.5
# ====================================================================================================>


# Autor rozwiązania Piotr Polański
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:  # do tego momentu eliminujemy l. parzyste
        return True
    if n % 2 == 0:
        return False
    d = 3
    s = sqrt(n)
    while d <= s:
        if n % d == 0:
            return False
        d += 2
    return True


def best(T):  # zwraca wyższy pierwszy wynik spośród 2 rozważanych przypadków
    l = len(T)
    case_one = T[0]
    d = 1
    while d < l:  # Działanie rozpoczęte dodawaniem: A + B * C + D...
        if d + 1 < l:
            case_one += T[d] * T[d + 1]
            d += 2
        if d + 1 == l:
            case_one += T[d]
            d += 1
    case_two = T[0] * T[1]
    d = 2
    while d < l:  # Działanie rozpoczęte mnożeniem: A * B + C * D...
        if d + 1 == l:
            case_two += T[d]
            d += 1
        if d + 1 < l:
            case_two += T[d] * T[d + 1]
            d += 2
    if not is_prime(
        case_one
    ):  # jeśli niepierwsze, zerujemy je. 0 oznacza że nie ma szans "wygrać" w funkcji (max)
        case_one = 0
    if not is_prime(case_two):
        case_two = 0
    return max(case_one, case_two)


def Zadanie_3A(T):
    l = len(T)
    out = 0
    for i in range(l - 1):  # min dł. podciągu 2
        for j in range(
            i + 1, l
        ):  # sprawdza wszystkie podciągi o danym początku i końcu
            val = (
                best(T[i : j + 1]) / (j - i + 1) if (j - i + 1) != l else 0
            )  # warunek na wypadek gdyby podciąg == ciąg. Dzielnik wyznaczamy z indeksów
            out = max(out, val)  # najwyższa wartość
    return out


