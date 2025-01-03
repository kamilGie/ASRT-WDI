from main_s import main_s
from _utils_S import parsuj_prototyp, main, podpowiedz, przykladowe_odpalenie


class Node:
    """lista dwukierunkowa, w zadaniach gdzie jest jednokierunkowa 2 kierunek"""

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next: Node | None = next
        self.prev: Node | None = prev
        if next:
            next.prev = self
        if prev:
            prev.next = self

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def lista_przesylaczowa():
    return """\n
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")\n\n\n\n\n\n
"""


class przesylaczowe_s(main_s):
    def __str__(self) -> str:
        res = parsuj_prototyp(self.linie_prototypu, self.funkcje, lista_przesylaczowa())

        cialo_maina = "\n"
        for funkcja in self.funkcje:
            cialo_maina += przykladowe_odpalenie(funkcja)
        cialo_maina += "\n\n"
        cialo_maina += podpowiedz()
        res += main(self.nr_zadania, cialo_maina)
        return res
