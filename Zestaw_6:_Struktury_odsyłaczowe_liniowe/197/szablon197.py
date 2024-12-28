# ====================================================================================================>
# Zadanie 197
# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę ele-
# mentów w cyklu.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def cycle_length(head)->int: ...






if __name__ == "__main__":
    from testy197 import odpal_testy


    cycle_length(Node(1, Node(2, Node(3))))


    # odpal_testy()
