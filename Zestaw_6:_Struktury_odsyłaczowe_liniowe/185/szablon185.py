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
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_185(p, key) -> Node: ...






if __name__ == "__main__":
    from testy185 import odpal_testy


    Zadanie_185(Node(1, Node(2, Node(3))), int(input('Podaj key: ')))


    # odpal_testy()
