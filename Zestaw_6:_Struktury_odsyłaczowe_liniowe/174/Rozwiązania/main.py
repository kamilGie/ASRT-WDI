# ====================================================================================================>
# Zadanie 174
# Zliczanie elementów łańcucha
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def policz(p: Node | None) -> int:
    count = 0
    while p is not None:
        count += 1
        p = p.next
    return count


