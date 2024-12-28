# ====================================================================================================>
# Zadanie 216
# Proszę napisać funkcję, która sprawdza czy dane drzewo jest poprawnym drzewem BST.
# ====================================================================================================>


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}"


def Zadanie_216(p, min_val=float("-inf"), max_val=float("inf")):
    if not p:
        return True
    if not (min_val < p.val < max_val):  #  poza dopuszczalnym zakresem
        return False
    return Zadanie_216(p.left, min_val, p.val) and Zadanie_216(p.right, p.val, max_val)


