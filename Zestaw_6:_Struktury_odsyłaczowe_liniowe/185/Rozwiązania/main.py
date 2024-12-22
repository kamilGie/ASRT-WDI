# ====================================================================================================>
# Zadanie 185
# Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy
# wskaźnik na początek listy oraz wartość klucza. Jeżeli element o takim kluczu występuje w liście należy go
# usunąć z listy. Jeżeli elementu o zadanym kluczu brak jest w liście należy element o takim kluczu wstawić
# do listy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_185(p, key) -> Node:
    head = prev = Node(key, p)  # wartownik z key
    while p:
        if p.val == key:  # znaleziono
            prev.next = p.next  # usuwam
            return head.next  # bez wartownika
        prev, p = p, p.next

    return head  # nie znaleziono zwracam z wartownikiem


