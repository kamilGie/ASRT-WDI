# ====================================================================================================>
# Zadanie 190
# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
# jednokierunkowej, przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_190(p)->Node: ...






if __name__ == "__main__":
    from testy190 import odpal_testy


    Zadanie_190(Node(1, Node(2, Node(3))))


    # odpal_testy()
