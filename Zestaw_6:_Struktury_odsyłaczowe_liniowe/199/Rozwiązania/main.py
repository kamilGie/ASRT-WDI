# ====================================================================================================>
# Zadanie 199
# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_199(head):
    slow = fast = head

    # Szukam punktu przecięcia w cyklu
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    before_cycle = None
    while head != fast:  #  przechodze przez head az zostanie elemetem cyklu
        before_cycle = head
        head = head.next

        fast = fast.next
        while fast != slow:  # przechodze przez cykl
            fast = fast.next
            if fast == head:  # head jest w cyklu zwracam ostatni element
                return before_cycle

    return before_cycle


