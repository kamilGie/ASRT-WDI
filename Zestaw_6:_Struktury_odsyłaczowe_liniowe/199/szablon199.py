# ====================================================================================================>
# Zadanie 199
# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_199(head)->Node: ...






if __name__ == "__main__":

    Zadanie_199(Node(1, Node(2, Node(3))))
