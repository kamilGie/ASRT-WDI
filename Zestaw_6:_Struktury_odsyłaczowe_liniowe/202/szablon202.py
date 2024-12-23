# ====================================================================================================>
# Zadanie 202
# Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W pierwszej
# liście liczby są posortowane rosnąco, a w drugiej nie. Proszę napisać funkcję usuwającą z obu list liczby
# występujące w obu listach. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
# łączną liczbę usuniętych elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_202(p, q)->int: ...






if __name__ == "__main__":
    from testy202 import odpal_testy


    Zadanie_202(Node(1, Node(2, Node(3))), Node(1, Node(2, Node(3))))


    # odpal_testy()
