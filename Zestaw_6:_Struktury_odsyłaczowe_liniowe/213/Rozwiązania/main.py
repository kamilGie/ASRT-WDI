# ====================================================================================================>
# Zadanie 213
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init(self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto pewną
# liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która uzupeł-
# nia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja powinna
# zwrócić liczbę wstawionych elementów. Można założyć, że lista wejściowa liczy więcej niż 2 elementy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def arithmetic_difference(p):
    value_nwd = 1
    r = p.next.val - p.val

    while p.next:
        value_nwd = NWD(r, (p.next.val - p.val))
        p = p.next
    return value_nwd


def repair(p):
    step = arithmetic_difference(p)

    inserted_count = 0
    while p.next:
        if ( p.val + step != p.next.val):  # jesli krokiem nie dotarlem do nastpnego elemetu musze go dodac
            p.next = Node(p.val + step, p.next)
            inserted_count += 1
        p = p.next
    return inserted_count


