# ====================================================================================================>
# Zadanie 189
# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
# jednokierunkowej,usuwa z niejwszystkie elementy, w których wartość klucza w zapisie trójkowym ma większą
# ilość jedynek niż dwójek.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def czy_usunac(val):
    cnt = [0, 0, 0]
    while val:
        cnt[val % 3] += 1
        val //= 3
    return cnt[1] > cnt[2]


def Zadanie_189(head):
    head = p = Node(0, head)  # pomocniczy poczatek
    while p.next:
        if czy_usunac(p.next.val):
            p.next = p.next.next
        else:
            p = p.next
    return head.next  # usuwanie poczatku


