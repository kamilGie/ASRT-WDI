# ====================================================================================================>
# Zadanie 200
# Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji
# należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.
# ====================================================================================================>
# zawieranie dosłowne nie wartościowe


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_200(p, q): ...






if __name__ == "__main__":
    from testy200 import odpal_testy


    Zadanie_200(Node(1, Node(2, Node(3))), Node(1, Node(2, Node(3))))


    # odpal_testy()
