# ====================================================================================================>
# Zadanie 188
# Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
# wartościach typu int, usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość bezpośrednio
# następujących po nich elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_188(head):
    while head.next and (head.val == 0 or head.next.val % head.val == 0):
        head = head.next
    if head.next:
        head.next = Zadanie_188(head.next)
    return head


