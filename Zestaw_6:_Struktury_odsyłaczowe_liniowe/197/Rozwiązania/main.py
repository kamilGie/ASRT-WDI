# ====================================================================================================>
# Zadanie 197
# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę ele-
# mentów w cyklu.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def cycle_length(head):
    slow = head
    fast = head

    while True:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # Cykl wykryty
            length = 1
            current = slow.next
            while current != slow:  # licze po ilu przejsciach `slow` dotrze do `fast`
                current = current.next
                length += 1
            return length


