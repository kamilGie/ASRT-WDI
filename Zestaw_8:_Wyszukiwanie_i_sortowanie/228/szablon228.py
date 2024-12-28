# ====================================================================================================>
# Zadanie 228
# Dana jest lista odsyłaczowa przechowująca liczby całkowite. Proszę napisać funkcję wypi-
# nającą maksymalny element z listy, a następnie zrealizować funkcję sortowania przez wybieranie (selection
# sort)
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")







# funkcja pomocnicza testy nie beda obejmowac
def remove_max(head): ...



def selection_sort(head) -> Node: ...






if __name__ == "__main__":
    from testy228 import odpal_testy


    selection_sort(Node(1, Node(2, Node(3))))


    remove_max(Node(1, Node(2, Node(3))))


    # odpal_testy()
