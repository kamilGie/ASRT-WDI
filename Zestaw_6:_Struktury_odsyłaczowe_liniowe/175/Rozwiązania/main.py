# ====================================================================================================>
# Zadanie 175
# Proszę zaimplementować zbiór mnogościowy liczb naturalnych korzystając ze struktury
# listy odsyłaczowej.
# • czy element należy do zbioru
# • wstawienie elementu do zbioru
# • usunięcie elementu ze zbioru
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def contains(head, value) -> bool:
    while head:
        if head.val == value:
            return True
        head = head.next
    return False


def insert(head, value) -> Node:
    return Node(value, head) if not contains(head, value) else head


def delete_node(head, value) -> Node:
    if head.val == value:  # wartość jest pierwsza
        return head.next

    prev, current = Node(0, head), head  # prev na wartowniku
    while current:
        if current.val == value:
            prev.next = current.next
            return head  # znaleziono usunieto
        prev = current
        current = current.next

    return head  # nie bylo value


