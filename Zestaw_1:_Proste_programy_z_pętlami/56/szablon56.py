# ====================================================================================================>
# Zadanie 56
# „Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych
# cyfr,gdzieM,N >=0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
# pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0 gdy taka liczba nie istnieje. Na
# przykład dla liczby 1202742516 spośród obciętych liczb pierwszych:2,5,7,251,2027 liczbą spełniającą warunek
# jest liczba 251.
# ====================================================================================================>


def Zadanie_56(K): ...


if __name__ == "__main__":
    from testy56 import odpal_testy, podpowiedz

    Zadanie_56(1202742516)  # return 251

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
