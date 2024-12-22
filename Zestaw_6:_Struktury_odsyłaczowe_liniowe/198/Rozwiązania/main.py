# ====================================================================================================>
# Zadanie 198
# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę ele-
# mentów przed cyklem.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_198(head):
    slow = fast = head

    # Szukam punktu przecięcia w cyklu
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    before_cycle = 0
    while head != fast:  #  przechodze przez head az zostanie elemetem cyklu
        head = head.next
        before_cycle += 1

        fast = fast.next
        while fast != slow:  # przechodze przez cykl
            if fast == head:  # head jest w cyklu zwracam dlugosci
                return before_cycle
            fast = fast.next

    return before_cycle


