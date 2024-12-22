# ====================================================================================================>
# Zadanie 184
# Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
# dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_184(p, q): ...






if __name__ == "__main__":
    from testy184 import odpal_testy


    Zadanie_184(Node(1, Node(2, Node(3))), Node(1, Node(2, Node(3))))


    # odpal_testy()
