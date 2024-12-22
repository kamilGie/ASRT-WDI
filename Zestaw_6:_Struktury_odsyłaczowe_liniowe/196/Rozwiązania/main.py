# ====================================================================================================>
# Zadanie 196
# Dana jest lista, który być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_196(head):
    """Floyd's Cycle Detection"""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next  # Przesunięcie o 1 krok
        fast = fast.next.next  # Przesunięcie o 2 kroki

        if slow == fast:  # Jeśli wskaźniki się spotykają, cykl istnieje
            return True

    return False  # Jeśli fast osiągnie None, brak cyklu


