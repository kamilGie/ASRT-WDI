# ====================================================================================================>
# Zadanie 191
# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listydwukierunkowej,
# usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next: Node | None = next
        self.prev: Node | None = prev
        if next:
            next.prev = self
        if prev:
            prev.next = self

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def even_ones_in_bin(val):
    even = True
    while val:
        if val % 2 == 1:
            even = not even
        val //= 2
    return even


def Zadanie_191(head):
    dummy = Node(0, head, None)  # wartownik
    current = head

    while current:
        if not even_ones_in_bin(current.val):
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        current = current.next

    return dummy.next


