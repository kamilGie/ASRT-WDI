# ====================================================================================================>
# Zadanie 174
# Zliczanie elementów łańcucha
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")










def policz(p: Node | None) -> int: ...








if __name__ == "__main__":
    from testy174 import odpal_testy


    policz(Node(1, Node(2, Node(3))))


    # odpal_testy()
