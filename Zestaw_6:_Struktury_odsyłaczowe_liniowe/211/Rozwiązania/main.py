# ====================================================================================================>
# Zadanie 211
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init (self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawiera wartości będące liczbami naturalnymi Proszę napisać funkcję repair(p), (p wskazuje na
# pierwszy element listy) która przekształca listę tak aby liczby parzyste znalazły się na końcu listy. Funk-
# cja powinna zwrócić wskazanie na przekształconą listę. Można założyć, że lista wejściowa liczy więcej niż 2
# elementy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def repair(p) -> Node:
    """bede tworzyl 2 lancuchy ktore potem zlacze"""
    odd_head = odd_tail = Node(0)
    even_head = even_tail = Node(0)

    while p:
        if p.val % 2 == 1:  # nieparzysta dołączam do odd_tail
            odd_tail.next = p
            odd_tail = odd_tail.next
        else:  # parzysta dołączam do even_tail
            even_tail.next = p
            even_tail = even_tail.next
        p = p.next

    # Doczepiam listę parzystą na koniec listy nieparzystej
    odd_tail.next = even_head.next
    even_tail.next = None
    return odd_head.next  # bez wartownika


