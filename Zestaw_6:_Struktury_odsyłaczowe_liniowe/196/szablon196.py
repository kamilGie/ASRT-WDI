# ====================================================================================================>
# Zadanie 196
# Dana jest lista, który być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_196(head): ...






if __name__ == "__main__":
    from testy196 import odpal_testy


    Zadanie_196(Node(1, Node(2, Node(3))))


    # odpal_testy()
