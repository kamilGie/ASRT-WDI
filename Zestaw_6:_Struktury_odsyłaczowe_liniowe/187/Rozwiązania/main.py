# ====================================================================================================>
# Zadanie 187
# Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
# wartościach typu int, usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio
# poprzedzających je elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_187(head):
    current = head
    while current.next:
        if current.next.val < current.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


