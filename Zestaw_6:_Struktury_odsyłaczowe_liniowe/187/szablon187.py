# ====================================================================================================>
# Zadanie 187
# Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
# wartościach typu int, usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio
# poprzedzających je elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_187(head)->Node: ...






if __name__ == "__main__":
    from testy187 import odpal_testy


    Zadanie_187(Node(1, Node(2, Node(3))))


    # odpal_testy()
