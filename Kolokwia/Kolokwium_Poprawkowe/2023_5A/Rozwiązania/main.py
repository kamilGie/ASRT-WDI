# ====================================================================================================>
# Zadanie 5A, 2024-02-06
# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T),
# która znajdzie w tablicy największy kwadrat, złożony wyłącznie z elementów, które w zapisie ósemkowym złożone są z niepowtarzających się cyfr. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić długość boku znalezionego kwadratu. Kwadrat 1 × 1 też jest kwadratem. W przypadku
# nieznalezienia żadnego kwadratu należy zwrócić wartość 0. Dane wejściowe w tablicy mają pozostać
# niezniszczone.
# ====================================================================================================>


def distinct_octal(x):
    digits_appear = [False] * 8
    while x:
        x, d = divmod(x, 8)
        if digits_appear[d]:  # Jeśli cyfra już wystąpiła
            return False
        digits_appear[d] = True  # Zaznacz cyfrę jako używaną
    return True


def square(T):
    n = len(T)
    B = [[distinct_octal(T[i][j]) for j in range(n)] for i in range(n)]  # Tablica booli
    D = [[0] * n for _ in range(n)]  # Tablica przechowująca rozmiary kwadratów
    res = 0

    for i in range(n):
        for j in range(n):
            if B[i][j]:  # Jeśli liczba spełnia warunek
                if i == 0 or j == 0:
                    D[i][j] = 1  # Na brzegu wszystkie wartości mają bok 1
                else:
                    # Minimalna z trzech sąsiednich wartości plus 1
                    D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
                res = max(res, D[i][j])  # Aktualizacja maksymalnego boku
    return res


