# ====================================================================================================>
# Zadanie 201
# Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do
# funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do
# scalonej listy. Zadanie należy wykonać jako funkcję iteracyjną, a następnie jako funkcję rekurencyjną.
# ====================================================================================================>
# posortowane rosąco


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def iteration(p, q): ...



def recursive(p, q): ...






if __name__ == "__main__":
    from testy201 import odpal_testy


    iteration(Node(1, Node(2, Node(3))), Node(1, Node(2, Node(3))))


    recursive(Node(1, Node(2, Node(3))), Node(1, Node(2, Node(3))))


    # odpal_testy()
