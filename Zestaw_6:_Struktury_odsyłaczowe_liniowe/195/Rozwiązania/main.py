# ====================================================================================================>
# Zadanie 195
# Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą.
# Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia
# jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_195(current):
    head = current = Node(None, current)  # wartownik
    bestlen = 0  # najdluzszy podciag
    start = end = None  # pierwszy i ostatni element lancycha najdluzszego podciagu

    while current and current.next:
        prev, current = current, current.next

        cnt = 1
        while current.next and current.val < current.next.val:  # rosnie
            cnt += 1
            current = current.next

        if cnt == bestlen:  # podciag ma byc unikalny
            start = end = None  # usuwam znaleziony podciag
        elif cnt > bestlen:
            bestlen = cnt
            start, end = prev, current.next

    if start:  # istnieje podciag
        start.next = end

    return head.next  # pozbywamy się wartownika


