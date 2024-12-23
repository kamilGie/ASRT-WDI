# ====================================================================================================>
# Zadanie 128
# Dana jest tablica T[N][N] wypełniona wartościami 0,1. Każdy wiersz tablicy traktujemy
# jako liczbę zapisaną w systemie dwójkowy m o długości N bitów. Stała N jest rzędu 1000.
# Proszę zaimplementować funkcję distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych
# w wierszach liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość
# pomiędzy znalezionymi wierszami. Można założyć, że żadne dwa wierze nie zawierają identycznego ciągu
# cyfr.
# ====================================================================================================>

def bin_to_deci(row):
    result = 0
    power_of_two = 1

    for i in range(len(row) - 1, -1, -1):
        result += row[i] * power_of_two
        power_of_two *= 2  # Następna potęga dwójki

    return result


def distance(T):
    min_idx = max_idx = 0
    for i in range(1, len(T)):
        # leksykograficznie porównuje listy dokladnie tak jak chcemy
        if T[i] > T[max_idx]:
            max_idx = i
        elif T[i] < T[min_idx]:
            min_idx = i

    return bin_to_deci(T[max_idx]) - bin_to_deci(T[min_idx])
