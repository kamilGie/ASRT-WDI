# ====================================================================================================>
# Zadanie 173
# wypisywanie elementów łańcucha
# ====================================================================================================>


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev: Node | None = prev
        self.next: Node | None = next


def wypis(p):  # z wykladu
    while p:
        print(p.val)
        p = p.next
