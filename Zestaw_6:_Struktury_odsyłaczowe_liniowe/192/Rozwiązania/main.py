# ====================================================================================================>
# Zadanie 192
# Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def delete_key(p, key):
    dummy = Node(0, p)
    current = dummy
    while current.next:
        if current.next.val == key:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next


def Zadanie_192(head):
    """Dla kazdej wartosci przechodze w przod i usuwam jej wystapienia"""
    current = head
    while current:
        current.next = delete_key(current.next, current.val)
        current = current.next

    return head


