# ====================================================================================================>
# Zadanie A5, 17.01.2023
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi, na której możemy wykonywać operacje:
# • rotacji elementów danego wiersza w prawo,
# • rotacji elementów danej kolumny w dół.
# Tablicę taką nazywamy kwadratem magicznym, wtedy gdy suma elementów w każdym wierszu i każdej kolumnie jest jednakowa. Proszę napisać funkcję magic(T), która sprawdza czy po wykonaniu dokładnie dwóch
# dowolnych operacji tablica T stanie się kwadratem magicznym. Funkcja powinna zwrócić True albo F alse.
# Na przykład dla tablicy:
# 3 11 14 17
# 6 12 7 9
# 10 8 16 13
# 5 15 4 2
# po wykonaniu rotacji wiersza 0, następnie rotacji kolumny 2, tablica będzie kwadratem magicznym.
# ====================================================================================================>


def magic(T): ...


if __name__ == "__main__":
    from testy2022_A5 import odpal_testy, podpowiedz

    magic( [[3, 11, 14, 17], [6, 12, 7, 9], [10, 8, 16, 13], [5, 15, 4, 2]])  # return True

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
