# ====================================================================================================>
# Zadanie 183
# Dana jest nie pusta lista reprezentująca liczbę naturalną. Kolejnee lementy listy przechowują
# kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_183(p):
    def reverse_list(node):
        "Funkcja pomocnicza do odwracania listy"
        prev, current = None, node
        while current:
            next_node = current.next
            current.next = prev
            prev, current = current, next_node
        return prev

    current = head = reverse_list(p)
    carry = 1

    while current:
        # sprawdzam czy przeszlo dzielac przez 10
        carry, current.val = divmod(current.val + carry, 10)
        current = current.next

    # przywrócenie oryginalny porządku
    head = reverse_list(head)
    return head if not carry else Node(1, head)  # potrzeba zwieksznia cyfr liczby


