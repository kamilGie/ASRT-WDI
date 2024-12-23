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


def Zadanie_191(head)->Node: ...


if __name__ == "__main__":
    from testy191 import odpal_testy

    Zadanie_191(Node(1, Node(2, Node(3))))

    # odpal_testy()
