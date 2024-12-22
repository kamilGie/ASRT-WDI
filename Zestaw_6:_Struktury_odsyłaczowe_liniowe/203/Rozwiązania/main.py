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
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_203(p, q):
    dummy_p = Node(0, p)
    dummy_q = Node(0, q)

    prev_p, curr_p = dummy_p, p
    prev_q, curr_q = dummy_q, q

    removed_count = 0
    while curr_p and curr_q:

        if curr_p.val == curr_q.val:  # # Zachowujemy węzły w obu listach
            prev_p, curr_p = curr_p, curr_p.next
            prev_q, curr_q = curr_q, curr_q.next
        elif curr_p.val < curr_q.val:  # Usuń element z listy p
            prev_p.next = curr_p.next
            curr_p = curr_p.next
            removed_count += 1
        else:  # Usuń element z listy q
            prev_q.next = curr_q.next
            curr_q = curr_q.next
            removed_count += 1

    # Usuwanie pozostałych elementów z listy p
    prev_p.next = None
    while curr_p:
        removed_count += 1
        curr_p = curr_p.next

    # Usuwanie pozostałych elementów z listy q
    prev_q.next = None
    while curr_q:
        removed_count += 1
        curr_q = curr_q.next

    return removed_count


