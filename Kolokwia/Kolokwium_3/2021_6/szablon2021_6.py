# ====================================================================================================>
# Zadanie 6, 20 stycznia 2022
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
#     def __init__(self, val):
#     self.val = val
#     self.next = None
#
# Lista zawierała wartości stanowiące kolejne wyrazy ciągu geometrycznego. Z wnętrza listy usunięto
# pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy),
# która uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu geometrycznego.
# Funkcja powinna zwrócić liczbę wstawionych elementów. Na przykład poniższa lista zostanie przekształcona:
# 4 -32 -128 -2048 −→ 4 -8 16 -32 64 -128 256 -512 1024 -2048 (zostanie zwrócona wartość 6)
# Można założyć, że lista wejściowa liczy więcej niż 2 elementy i każdy element
# listy jest liczbą całkowitą rózną od 0 (iloraz ciągu nie musi być całkowity).
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def repair(p): ...


if __name__ == "__main__":
    from testy2021_6 import odpal_testy, podpowiedz

    repair(Node(4, Node(-32, Node(-128, Node(-2048)))))  # return 6

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
