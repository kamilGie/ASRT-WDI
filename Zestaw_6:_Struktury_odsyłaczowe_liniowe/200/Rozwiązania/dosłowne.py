# ====================================================================================================>
# Zadanie 200
# Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji
# należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.
# ====================================================================================================>
# zawieranie dosłowne nie wartościowe


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def contain(p, element):
    while p:
        if p == element:
            return True
        p = p.next
    return False


def Zadanie_200(p, q):
    """Aby sie zawieral jeden w drugim to jeden musi wskazywac na poczatek pierwszego"""
    return contain(p, q) or contain(q, p)
