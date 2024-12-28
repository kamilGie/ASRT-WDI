from _utils_S import parsuj_prototyp, main, podpowiedz, przykladowe_odpalenie
from main_s import main_s


def drzewo():
    return """\n\n\nclass Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}" \n\n\n\n\n\n
"""


class drzewo_s(main_s):
    def __str__(self) -> str:
        res = parsuj_prototyp(self.linie_prototypu, self.funkcje, drzewo())

        cialo_maina = "\n"
        for funkcja in self.funkcje:
            cialo_maina += przykladowe_odpalenie(funkcja)
        cialo_maina += "\n\n"
        cialo_maina += podpowiedz()
        res += main(self.nr_zadania, cialo_maina)
        return res
