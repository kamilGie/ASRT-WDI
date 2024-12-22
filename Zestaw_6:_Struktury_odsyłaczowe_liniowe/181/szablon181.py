# ====================================================================================================>
# Zadanie 181
# Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wska-
# zanie na pierwszy element listy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def remove_last(p) -> Node: ...






if __name__ == "__main__":
    from testy181 import odpal_testy


    remove_last(Node(1, Node(2, Node(3))))


    # odpal_testy()
