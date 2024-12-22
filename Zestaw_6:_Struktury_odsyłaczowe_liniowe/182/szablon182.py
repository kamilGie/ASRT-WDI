# ====================================================================================================>
# Zadanie 182
# Dana jest nie pusta lista, proszę napisać funkcję usuwającą co drugie element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_182(p) -> Node: ...






if __name__ == "__main__":
    from testy182 import odpal_testy


    Zadanie_182(Node(1, Node(2, Node(3))))


    # odpal_testy()
