# ====================================================================================================>
# Zadanie 78
# Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
# równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
# ====================================================================================================>


def Zadanie_78(t):
    n = len(t)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + t[i]

    best = 0
    for i in range(n):
        for j in range(i, n):
            if j > i and t[j] <= t[j - 1]:
                break
            sub_sum = s[j + 1] - s[i]
            idx_sum = (j * (j + 1)) // 2 - (i * (i - 1)) // 2
            if sub_sum == idx_sum:
                best = max(best, j - i + 1)
    return best


