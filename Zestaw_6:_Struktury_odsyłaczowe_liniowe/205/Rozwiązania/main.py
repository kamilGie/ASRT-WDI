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
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_205(head, p, q) -> int:
    deleted_cnt = 0
    while head:
        next_node = head.next
        head.next = None
        if head.val > 0 and head.val % 2 == 0:  # przypisanie p
            p.next = head
            p = p.next
        elif head.val < 0 and head.val % 2 == 1:  # przypisanie q
            q.next = head
            q = q.next
        else:  # usuwanie z pamieci
            deleted_cnt += 1

        head = next_node

    return deleted_cnt
