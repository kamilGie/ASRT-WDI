# ====================================================================================================>
# Zadanie 6 2020
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node
# def init(self,val):
#    self.val = val
#    self.next = None
#
# Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o uporządkowanych rosnąco elementach.
# Proszę napisać funkcję iloczyn(z1,z2,z3), która przekształca 3 listy (zbiory) z1,z2,z3 w jedną
# listę (zbiór) zawierającą elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić
# wskazanie do listy wynikowej.
# Komentarz: Zadanie jest tak proste, że nie wymaga przykładu ani danych testowych.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def iloczyn(z1, z2, z3): ...


if __name__ == "__main__":
    from testy2020_6 import odpal_testy, podpowiedz

    iloczyn(Node(1, Node(3)), Node(1, Node(2)), Node(1, Node(2,Node(3))))  # return 1

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
