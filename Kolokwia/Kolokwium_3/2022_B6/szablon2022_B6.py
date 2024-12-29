# ====================================================================================================>
# Zadanie B6, 19.01.2023
# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola key i next, której węzły
# przechowują liczby całkowite. Proszę napisać funkcję separate(p) która rozdziela listę cykliczną na dwie
# listy cykliczne. Pierwsza powinna zawierać klucze parzyste dodatnie, druga klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać wskaźniki na listę z danymi. Funkcja
# powinna zwrócić wskaźniki na powstałe listy oraz liczbę usuniętych elementów.
# ====================================================================================================>


class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

    def __str__(self):
        result = []
        start = self
        while start:
            result.append(str(start.key))
            start = start.next
            if start == self:  # Zakończenie cyklu
                result.append("(cykl)")
                break
        return " -> ".join(result)





def separate(p): ...







if __name__ == "__main__":
    from testy2022_B6 import odpal_testy, podpowiedz

    p = Node( 1, Node( -1, Node(2, Node(-2, Node(3, Node(-3, Node(4, Node(-4, Node(5, Node(-5)))))))),),)
    p.next.next.next.next.next.next.next.next.next.next = p
    separate(p)  # return (even_node, odd_node, 5)

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
