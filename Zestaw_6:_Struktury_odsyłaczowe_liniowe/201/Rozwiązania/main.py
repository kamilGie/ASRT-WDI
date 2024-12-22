# ====================================================================================================>
# Zadanie 201
# Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do
# funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do
# scalonej listy. Zadanie należy wykonać jako funkcję iteracyjną, a następnie jako funkcję rekurencyjną.
# ====================================================================================================>
# posortowane rosąco


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def iteration(p, q):
    head = tail = Node(0)  # wartownik
    while p and q:
        if p.val < q.val:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next
        tail = tail.next

    # Dodanie pozostałych elementów
    tail.next = p if p else q
    return head.next  # bez wartownika


def recursive(p, q):
    if not p:
        return q
    if not q:
        return p

    if p.val < q.val:
        p.next = recursive(p.next, q)
        return p
    else:
        q.next = recursive(p, q.next)
        return q


