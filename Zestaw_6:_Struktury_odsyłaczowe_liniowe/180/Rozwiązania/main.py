# ====================================================================================================>
# Zadanie 180
# Proszę napisać funkcję wstawiającą na koniec listy nowy element.
# Do funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą wartość.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def push_back(p, val) -> Node:
    head = p
    while p.next:
        p = p.next
    p.next = Node(val)
    return head


