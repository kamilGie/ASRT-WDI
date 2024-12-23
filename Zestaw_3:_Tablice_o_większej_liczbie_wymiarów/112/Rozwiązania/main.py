# ====================================================================================================>
# Zadanie 112
# Dana jest plansza o wymiarach NxN zawierająca wartości 0 i 1. Pola o wartości 1 zawierają
# pułapki.Skoczek musi dotrzeć z górnego wiersza planszy do dolnego. Każdy ruch skoczka musi go przybliżać do dolnego wiersza.
# Proszę napisać program, który zwraca długość najkrótszej bezpiecznej drogi skoczka z wiersza górnego do wiersza dolnego.
# ====================================================================================================>
# return dlugosci najkroszedj drogi  - jak sie da
# return False - jak sie nie da

from math import inf


def Zadanie_112(T):
    N = len(T)
    skoki = [(1, -2), (2, -1), (2, 1), (1, 2)]  # Skoki przybliżające do dolnego wiersza

    # Inicjalizacja tablicy odległości
    min_odległość = [[inf] * N for _ in range(N)]
    min_odległość[0] = [0] * N  # Pierwszy wiersz jest początkowo dostępny

    # Iteracja przez wiersze tablicy
    for y in range(N - 1):
        for x in range(N):
            if min_odległość[y][x] == inf:
                continue  # Pole niedostępne, pomijamy

            for dy, dx in skoki:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and T[ny][nx] == 0:  # Sprawdzamy zakres i brak pułapki
                    min_odległość[ny][nx] = min(min_odległość[ny][nx], min_odległość[y][x] + 1)

    # Znalezienie minimalnej odległości do dolnego wiersza
    wynik = min(min_odległość[N - 1])

    return wynik if wynik < inf else False
