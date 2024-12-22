# ====================================================================================================>
# Zadanie 192
# Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_192(head): ...






if __name__ == "__main__":
    from testy192 import odpal_testy


    Zadanie_192(Node(1, Node(2, Node(3))))


    # odpal_testy()
