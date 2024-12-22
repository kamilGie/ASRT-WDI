# ====================================================================================================>
# Zadanie 208
# Proszę napisać funkcję, która usuwa z listy cyklicznej elementy, których klucz występuje
# dokładnie k razy. Do funkcji należy przekazać wskazanie na jeden z elementów listy, oraz liczbę k, funkcja
# powinna zwrócić informację czy usunięto jakieś elementy z listy.
# ====================================================================================================>
# zakladam ze lista jest cykliczna od poczatku  bez lancuchow przed cyklem


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_208(p, k):
    current = p
    counter = {}
    while True:  # zliczam wystapienia kazdej wartosci
        counter[current.val] = counter.get(current.val, 0) + 1
        current = current.next
        if current == p:  # przeszedlem cykl
            break

    removed = False
    prev = Node(None, current)
    while True:  # jesli wartosci wystapila k razy to usuwam z listy
        if counter[current.val] == k:
            prev.next = current.next
            removed = True
        else:  # nie usunalem wiec mozna przesunac prev na current
            prev = current

        current = current.next

        if current == p:  # przeszedlem cykl
            return removed


