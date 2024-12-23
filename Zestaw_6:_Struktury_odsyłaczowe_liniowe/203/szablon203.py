# ====================================================================================================>
# Zadanie 203
# Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W obu listach
# liczby są posortowane rosnąco. Proszę napisać funkcję usuwającą z każdej listy liczby nie występujące w
# drugiej.Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę usuniętych
# elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_203(p, q)->int: ...






if __name__ == "__main__":
    from testy203 import odpal_testy


    Zadanie_203(Node(1, Node(2, Node(3))), Node(1, Node(2, Node(3))))


    # odpal_testy()
