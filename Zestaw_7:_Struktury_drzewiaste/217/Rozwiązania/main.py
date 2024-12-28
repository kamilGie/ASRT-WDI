# ====================================================================================================>
# Zadanie 217
# Proszę napisać funkcję, która sprawdza czy dana liczba należy do drzewa BST. Funkcję
# proszę zrealizować jako funkcję rekurencyjną, a następnie jako funkcję bez użycia rekurencji.
# ====================================================================================================>


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}"

def Zadanie_217_rek(p, val):
    if not p:
        return False
    if p.val == val:
        return True

    return ( Zadanie_217_rek(p.left, val) if val < p.val else Zadanie_217_rek(p.right, val))


def Zadanie_217_iter(p, val):
    while p:
        if p.val == val:
            return True
        p = p.left if val < p.val else p.right
    return False


