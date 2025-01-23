# ====================================================================================================>
# Zadanie 5A, 2024-02-06
# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T),
# która znajdzie w tablicy największy kwadrat, złożony wyłącznie z elementów, które w zapisie ósemkowym złożone są z niepowtarzających się cyfr. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić długość boku znalezionego kwadratu. Kwadrat 1 × 1 też jest kwadratem. W przypadku
# nieznalezienia żadnego kwadratu należy zwrócić wartość 0. Dane wejściowe w tablicy mają pozostać
# niezniszczone.
# ====================================================================================================>


def square(T): ...


if __name__ == "__main__":
    from testy2023_5A import odpal_testy, podpowiedz

    square([ [ 1 ,1 ,1] , [1,9,1],[1,1,1]])  # return 1

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
