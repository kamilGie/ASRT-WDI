# ====================================================================================================>
# Zadanie 178
# Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def reverse(head): ...






if __name__ == "__main__":
    from testy178 import odpal_testy


    reverse(Node(1, Node(2, Node(3))))


    # odpal_testy()
