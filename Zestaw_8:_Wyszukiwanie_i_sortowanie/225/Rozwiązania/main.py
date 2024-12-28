# ====================================================================================================>
# Zadanie 225
# Dana jest tablica T[N] wypełniona liczbami nieujemnymi. Wartości 0 oznaczają dziury w
# których nie można przechowywać liczb naturalnych. Proszę napisać funkcję sortującą taką tablice.
# ====================================================================================================>


def sort(T):
    """Quicksort"""
    # Warunek zakończenia rekurencji
    if len(T) <= 1:
        return T

    # Wybór pivota (środkowy element)
    pivot = T[len(T) // 2]

    # Podział na trzy części: mniejsze, równe, większe
    less = [x for x in T if x < pivot]
    equal = [x for x in T if x == pivot]
    greater = [x for x in T if x > pivot]

    # Rekurencyjne sortowanie części "less" i "greater"
    return sort(less) + equal + sort(greater)


def Zadanie_225(T):
    # Wartości różne od zera
    non_zero_values = [x for x in T if x != 0]

    # Sortuje wartosci rozne od zera
    sorted = sort(non_zero_values)

    # Wstawiamy posortowane wartości z powrotem
    idx = 0
    for i in range(len(T)):
        if T[i] != 0:
            T[i] = sorted[idx]
            idx += 1

    return T


