# ====================================================================================================>
# Zadanie 184
# Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
# dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_184(p, q):
    def reverse_list(node):
        "Funkcja pomocnicza do odwracania listy"
        prev, current = None, node
        while current:
            next_node = current.next
            current.next = prev
            prev, current = current, next_node
        return prev

    p, q = reverse_list(p), reverse_list(q)
    current = head = Node(0)  # pomocnicze Node
    carry = 0

    while p or q or carry:
        p_val = p.val if p else 0
        q_val = q.val if q else 0

        total = p_val + q_val + carry
        carry, value = divmod(total, 10)

        current.next = Node(value)  # tworze nowy lancuch z wartoscia
        current = current.next

        if p:
            p = p.next
        if q:
            q = q.next

    return reverse_list(head.next)  # usuwam pomocniczy node


