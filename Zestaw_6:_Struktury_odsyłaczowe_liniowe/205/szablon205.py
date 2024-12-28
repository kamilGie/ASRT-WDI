# ====================================================================================================>
# Zadanie 205
# Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza powinna zawierać klucze
# parzyste dodatnie, drugi klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. Do funkcji
# należy przekazać wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja powinna zwrócić
# liczbę usuniętych elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")






def Zadanie_205(head, p, q) -> int: ...






if __name__ == "__main__":
    from testy205 import odpal_testy

    head = Node( 1, Node( -1, Node(2, Node(-2, Node(3, Node(-3, Node(4, Node(-4, Node(5, Node(-5))))))))))
    p, q = Node(0), Node(0)
    print(Zadanie_205(head, p, q))

    odpal_testy()
