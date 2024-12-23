# ====================================================================================================>
# Zadanie 183
# Dana jest nie pusta lista reprezentująca liczbę naturalną. Kolejnee lementy listy przechowują
# kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.
# ====================================================================================================>
# 1 -> 2 ->3 symbolizuje 123

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_183(p): ...






if __name__ == "__main__":
    from testy183 import odpal_testy


    Zadanie_183(Node(1, Node(2, Node(3))))


    # odpal_testy()
