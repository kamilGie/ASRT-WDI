# ====================================================================================================>
# Zadanie 194
# Dana jest lista zawierająca ciąg obu stronnie domkniętych przedziałów. Krańce przedziałów
# określa uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję redukującą
# liczbę elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany
# do listy: [13,19] [2,6] [7,12]
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_194(head):
    p = head
    while p:
        prev, current = p, p.next

        while current:
            if current.val[0] <= p.val[1] and p.val[0] <= current.val[1]:  # przecinja sie zbiory
                p.val[0] = min(p.val[0], current.val[0])  # laczymy zbiory
                p.val[1] = max(p.val[1], current.val[1])
                prev.next = current.next  # Pominięcie węzła

            prev, current = current, current.next

        p = p.next

    return head


