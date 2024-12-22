# ====================================================================================================>
# Zadanie 179
# Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według
# ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która
# jest posortowana niemalejąco według ostatniej cyfry pola val.
# ====================================================================================================>
# zwrocic ta liste z 2 kroku


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_179(head) -> Node: ...






if __name__ == "__main__":
    from testy179 import odpal_testy


    Zadanie_179(Node(1, Node(2, Node(3))))


    # odpal_testy()
