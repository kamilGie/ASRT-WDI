# ====================================================================================================>
# Zadanie 178
# Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def reverse(head):
    """odwraca kazdy wskaznik pokolei"""
    prev, curr = None, head
    while curr:
        next_node = curr.next  # Zachowaj wskaźnik na kolejny węzeł
        curr.next = prev  # Odwróć wskaźnik
        prev, curr = curr, next_node  # Przesuń wskaźniki
    return prev


