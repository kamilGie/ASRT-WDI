# ====================================================================================================>
# Zadanie 5, 20 stycznia 2022
# Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
# dokładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N][N]
# zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
# sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
# dokładnie z 3 liczbami czynnikowo-podobnymi.
# ====================================================================================================>


def three(T): ...


if __name__ == "__main__":
    from testy2021_5 import odpal_testy, podpowiedz

    three([[14, 24, 14], [24, 24, 24], [24, 24, 14]])  # return 1

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
