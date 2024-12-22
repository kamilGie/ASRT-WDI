# ====================================================================================================>
# Zadanie 182
# Dana jest nie pusta lista, proszę napisać funkcję usuwającą co drugie element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_182(p) -> Node:
    head = p
    while p and p.next:
        p.next = p.next.next
        p = p.next
    return head


