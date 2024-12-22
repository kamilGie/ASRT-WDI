# ====================================================================================================>
# Zadanie 204
# Dane są dwie nie puste listy, z których każda zawiera nie powtarzające się elementy. Elementy
# wpierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej kolejności.Proszę
# napisać funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane elementy będą stanowić
# sumę mnogościową elementów z list wejściowych. Do funkcji należy przekazać wskazania na obie listy, funkcja
# powinna zwrócić wskazanie na listę wynikową. Na przykład dla list:
# 2→3→5→7→11
# 8→2→7→4
# powinna pozostać lista:
# 2→3→4→5→7→8→11
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


from math import inf


def Zadanie_204(p, q):
    # Wskaźnik z wartonikiem -inf by kazde elemetny q mniejsze od pierwszego p mogly sie wpisac przed -inf
    head_p = Node(-inf, p)
    current_q = q

    while current_q:
        prev_p, current_p = head_p, head_p.next

        # Zwiekszam current_p aż nie bedzię wieksze od current_q bo p jest posortowane
        while current_p and current_p.val <= current_q.val:
            prev_p = current_p
            current_p = current_p.next

        if prev_p.val < current_q.val:  # moge wpisac
            prev_p.next = Node(current_q.val, prev_p.next)

        current_q = current_q.next

    return head_p.next


