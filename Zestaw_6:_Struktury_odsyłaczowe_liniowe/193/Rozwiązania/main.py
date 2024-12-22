# ====================================================================================================>
# Zadanie 193
# Elementy w liście są uporządkowane według wartości klucza. Proszę napisać funkcję usuwającą z listy
# elementy o nie unikalnym kluczu. Do funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_193(head):
    dummy = Node(0, head)
    current = dummy
    removed_count = 0

    while current.next and current.next.next:
        if current.next.val == current.next.next.val:
            duplicate_val = current.next.val
            while current.next and current.next.val == duplicate_val:
                current.next = current.next.next
                removed_count += 1
        else:
            current = current.next

    return removed_count


