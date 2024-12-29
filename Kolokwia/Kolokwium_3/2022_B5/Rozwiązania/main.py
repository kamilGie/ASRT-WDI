# ====================================================================================================>
# Zadanie B5, 19.01.2023
# Sudoku składa się kwadratu o wymiarach 9 × 9 podzielonego na 9 małych kwadratów o wymiarach 3 × 3.
# W poprawnym rozwiązaniu: w każdym wierszu, każdej kolumnie i każdym małym kwadracie znajdują się
# cyfry 1 − 9. W tablicy T[9][9] zawierającej poprawne rozwiązanie, ktoś je złośliwie uszkodził, zamieniając
# miejscami dwa małe kwadraty. Wiemy, że zamienione kwadraty leżały w różnych wierszach i różnych kolumnach. Zamiana spowodowała, że niektóre wiersze i niektóre kolumny zawierają powtarzające się cyfry.
# Proszę napisać funkcję repeair(T), która naprawi uszkodzoną tablicę. Do funkcji należy przekazać tablicę
# zawierającą uszkodzone rozwiązanie, funkcja powinna zwrócić informację czy zamiana dotyczyła środkowego
# małego kwadratu.
# Przykład: W poniższej tablicy zamieniono środkowy kwadrat z prawym dolnym.
#
# 8, 1, 2,  7, 5, 3,  6, 4, 9
# 9, 4, 3,  6, 8, 2,  1, 7, 5
# 6, 7, 5,  4, 9, 1,  2, 8, 3
#
# 1, 5, 4,  3, 6, 8,  8, 9, 6
# 3, 6, 9,  9, 1, 7,  7, 2, 1
# 2, 8, 7,  4, 5, 2,  5, 3, 4
#
# 5, 2, 1,  9, 7, 4,  2, 3, 7
# 4, 3, 8,  5, 2, 6,  8, 4, 5
# 7, 9, 6,  3, 1, 8,  1, 6, 9
# ====================================================================================================>


def isValid(a):
    """sprawdzam czy jakas liczba nie wystapila 2 razy w wierszu lub kolumnie"""
    for i in range(9):
        appear_row, appear_col = [False] * 10, [False] * 10 # 10 aby miec liczby 1-9 z niepotrzebnym 0
        for j in range(9):
            # liczba juz wystapila mamy powtorzenie
            if appear_row[a[i][j]] or appear_col[a[j][i]]:
                return False

            # dodaje do tablicy wystapien liczbe
            appear_row[a[i][j]] = appear_col[a[j][i]] = True

    return True


def swap(T, a, b):
    """ zamienia podkwadraty o indeksach a i b miejscami """
    # pozycje lewych górnych wierzchołków każdego podkwadratu
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    subgrid_offsets = [ (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2) ]
    for x, y in subgrid_offsets:
        T[ax + x][ay + y], T[bx + x][by + y] = T[bx + x][by + y], T[ax + x][ay + y]


def repair(T):
    # pozycje lewych górnych wierzchołków każdego podkwadratu
    subgrid_top_left_positions = [ (0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6) ]

    # sprawdzamy każdą parę
    for a in range(9):
        for b in range(a + 1, 9):
            swap(T, subgrid_top_left_positions[a], subgrid_top_left_positions[b])
            r = isValid(T)
            swap(T, subgrid_top_left_positions[a], subgrid_top_left_positions[b])
            # przywracamy oryginalną tablicę
            if r:
                return a == 4 or  b ==4
    return None  # niemożliwe dla poprawnych danych wejściowych


