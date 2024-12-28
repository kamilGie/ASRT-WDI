# ====================================================================================================>
# Zadanie 97
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.
# ====================================================================================================>
# return tablica T2

from math import inf


def Zadanie_97(T1):
    """Będę usuwał najmniejszy element z każdej tablicy, aż usunę wszystkie elementy, i sprawdzał powtarzalność tych najmniejszych elementów."""
    N = len(T1)
    T2 = []

    while True:
        # Szukam najmniejszego elementu na 0 indeksie kazdej tablicy jesli istenieje
        smallest = min((row[0] for row in T1 if row), default=inf)

        # jesli najmniejszy nie istenieje to znaczy ze przeszedlem wszystkie tablice
        if smallest == inf:
            break

        # Usuwam najmniejsze elementy i licze ich wystąpienia
        smallest_cnt = 0
        for row in T1:
            if row and row[0] == smallest:
                row.pop(0)
                smallest_cnt += 1

        # Dodaje singletony do wyniku
        if smallest_cnt == 1:
            T2.append(smallest)

    # Uzupełniam brakujące elementy zerami
    T2.extend([0] * (N * N - len(T2)))

    return T2
