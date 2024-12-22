# ====================================================================================================>
# Zadanie 179
# Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według
# ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która
# jest posortowana niemalejąco według ostatniej cyfry pola val.
# ====================================================================================================>
# zwrocic ta liste z 2 kroku


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_179(head) -> Node:

    heads = []
    tails = []
    for _ in range(10):  # 10 par podlist do przechowywania lancuchow
        sentinel = Node(0)  # węzeł-wartownik
        heads.append(sentinel)
        tails.append(sentinel)

    while head:
        last_digit = abs(head.val) % 10
        # Odcinamy węzeł od reszty listy i dołączamy do odpowiedniej podlisty
        next_node = head.next
        head.next = None
        tails[last_digit].next = head
        tails[last_digit] = head

        head = next_node

    result_tail = result_sentinel = Node(0)  # wartownik
    for i in range(10):
        if heads[i].next is not None:
            result_tail.next = heads[i].next
            result_tail = tails[i]

    return result_sentinel.next


