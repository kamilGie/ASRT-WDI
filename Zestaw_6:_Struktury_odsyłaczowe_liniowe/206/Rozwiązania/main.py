# ====================================================================================================>
# Zadanie 206
# Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w liście ułożone są
# według rosnących potęg. Proszę napisać funkcję obliczającą różnicę dwóch dowolnych wielomianów. Wielo-
# mianyreprezentowane są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo utworzonej
# listy reprezentującej wielomian wynikowy. Listy wejściowe powinny pozostać niezmienione.
# ====================================================================================================>
# p - q


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_206(p, q):
    head = tail = Node(0)
    while p or q:
        p_val = p.val if p else 0
        q_val = q.val if q else 0

        tail.next = Node(p_val - q_val)
        tail = tail.next

        if p: p = p.next
        if q: q = q.next

    return head.next


