# ====================================================================================================>
# Zadanie 200
# Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji
# należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def are_subsequences_equal(node1, sublist):
    while node1 and sublist:  # poki jedno sie nie skonczy
        if node1.val != sublist.val:  # roznia sie
            return False
        node1 = node1.next
        sublist = sublist.next
    return sublist is None  # Jeśli sublist się skończy, to była podlistą.


def contains_sublist(p, sublist):
    while p:
        if are_subsequences_equal(
            p, sublist
        ):  # czy sublista istnieje i zaczyna sie w p
            return True
        p = p.next
    return False


def Zadanie_200(p, q):
    return contains_sublist(p, q) or contains_sublist(q, p)
