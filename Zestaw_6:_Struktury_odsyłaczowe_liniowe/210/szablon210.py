# ====================================================================================================>
# Zadanie 210
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node
# ..def init(self,val):
# ....self.val = val
# ....self.next = None
# Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o uporządkowanych rosnąco elementach.
# Proszę napisać funkcję iloczyn(z1,z2,z3), która przekształca 3 listy(zbiory)z1,z2,z3 w jedną listę(zbiór)
# zawierającą elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić wskazanie do listy
# wynikowej.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def iloczyn(z1, z2, z3)->Node: ...






if __name__ == "__main__":
    from testy210 import odpal_testy


    iloczyn(int(input('Podaj z1: ')), int(input('Podaj z2: ')), int(input('Podaj z3: ')))


    # odpal_testy()
