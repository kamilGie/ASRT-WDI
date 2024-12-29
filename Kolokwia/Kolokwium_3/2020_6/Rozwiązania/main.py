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


def iloczyn(z1, z2, z3):
    head = tail = Node(0)  # Wartownik
    while z1 and z2 and z3:
        if z1.val == z2.val == z3.val:  # Istnieje przecięcie wszystkich trzech zbiorów
            tail.next = tail = Node(z1.val)
            z1, z2, z3 = z1.next, z2.next, z3.next
        else:  # Brak przecięcia, najmniejsza wartość zostaje odrzucona
            min_val = min(z1.val, z2.val, z3.val)
            if z1.val == min_val:
                z1 = z1.next
            if z2.val == min_val:
                z2 = z2.next
            if z3.val == min_val:
                z3 = z3.next

    return head.next


