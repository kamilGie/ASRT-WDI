# ====================================================================================================>
# Zadanie 198
# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę ele-
# mentów przed cyklem.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_198(head)->int: ...






if __name__ == "__main__":
    from testy198 import odpal_testy


    Zadanie_198(Node(1, Node(2, Node(3))))


    # odpal_testy()
