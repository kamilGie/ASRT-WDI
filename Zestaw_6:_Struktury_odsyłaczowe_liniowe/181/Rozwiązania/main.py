# ====================================================================================================>
# Zadanie 181
# Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wska-
# zanie na pierwszy element listy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def remove_last(p) -> Node:
    head = p
    while p.next.next:
        p = p.next
    p.next = None
    return head


