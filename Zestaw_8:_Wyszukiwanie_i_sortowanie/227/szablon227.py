# ====================================================================================================>
# Zadanie 227
# Dana jest lista odsyłaczowa przechowująca liczby całkowite. Proszę napisać funkcję wsta-
# wiającą istniejący element do posortowanej listy, a następnie zrealizować funkcję sortowania przez wstawianie
# (insertion sort).
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def insert_to_sorted(p, val): ...



def sort_by_insertion_sort(p): ...






if __name__ == "__main__":
    from testy227 import odpal_testy


    insert_to_sorted(Node(1, Node(2, Node(3))), int(input('Podaj val: ')))


    sort_by_insertion_sort(Node(1, Node(2, Node(3))))


    # odpal_testy()
