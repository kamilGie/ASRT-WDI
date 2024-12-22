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
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_202(p, q):
    head_p, head_q = Node(None, p), Node(None, q)  # Wskaźniki z wartonikami

    prev_q, current_q = head_q, q
    cnt = 0  # Licznik usuniętych elementów
    while current_q:
        prev_p = head_p
        current_p = head_p.next

        # Zwiekszam current_p aż nie bedzię mniejszę od current_q bo q jest posortowane
        while current_p and current_p.val < current_q.val:
            prev_p = current_p
            current_p = current_p.next

        if current_p and current_p.val == current_q.val:  # wartość jest w obu listach
            prev_p.next = current_p.next  # usuwam z dwoch list
            prev_q.next = current_q.next
            cnt += 2
        else:  # prev_q sie zmienia bo nie usunelismy current_q
            prev_q = current_q

        current_q = current_q.next

    return cnt


