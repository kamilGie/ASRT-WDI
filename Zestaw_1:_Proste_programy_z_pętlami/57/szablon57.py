# ====================================================================================================>
# Zadanie 57
# Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest
# liczbą pierwszą. Naprzykład: 13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo1∗3=3
# 16 jest  liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16=121(3) ,1∗2∗1=2 W liczbie naturalnej możemy
# dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092, 920. Proszę napisać funkcję, która dla
# danej liczby naturalnej N, zwróci najmniejszą podstawę systemu (z zakresu 2-16) w którym przynajmniej
# jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość None gdy taka podstawa nie istnieje.
# ====================================================================================================>


def Zadanie_57(N): ...


if __name__ == "__main__":
    from testy57 import odpal_testy, podpowiedz

    Zadanie_57(16)  # return 3

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
