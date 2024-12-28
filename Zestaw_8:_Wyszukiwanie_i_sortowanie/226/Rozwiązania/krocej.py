# ====================================================================================================>
# Zadanie 226
# Dany jest ciąg kwadratowych klocków. Każdy klocek ma kształt kwadratu pokolorowa-
# nego 4 kolorami. Klocki w ciągu mogą być dowolnie ustawione (przekręcone), a nawet odwrócone. Proszę
# napisać funkcję porządkującą klocki, tak aby identyczne klocki występowały obok siebie. Ciąg klocków jest
# reprezentowany jako tablica krotek, np. T = [(2,3,1,4), (3,2,4,1), (1,2,3,4), ...]
# ====================================================================================================>


def Zadanie_226(T):
    """Istnieją 3 różne klocki: (1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4). Reszta to ich modyfikacje."""

    def klucz(klocek):
        j = klocek.index(2)
        prev, next = klocek[(j - 1) % 4], klocek[(j + 1) % 4]
        if {prev, next} == {1, 3}:  # Opcja 1
            return 0
        elif {prev, next} == {3, 4}:  # Opcja 3
            return 2
        return 1  # Opcja 2

    T.sort(key=klucz)
