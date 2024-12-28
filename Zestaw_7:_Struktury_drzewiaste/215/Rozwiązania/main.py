# ====================================================================================================>
# Zadanie 215
# Proszę napisać następujące funkcje:
# 1. Funkcja, która usunie wszystkie węzły drzewa.
# 2. Funkcja, która usunie węzły powyżej n-tego poziomu.
# 3. Funkcja, która usunie wszystkie aktualne liście drzewa.
# ====================================================================================================>


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}"


def usun_wszystkie_wezly(p):
    if not p:
        return None
    p.left = usun_wszystkie_wezly(p.left)
    p.right = usun_wszystkie_wezly(p.right)
    return None  # Usuwam bieżący węzeł


def usun_wezly_powyzej_poziomu(p, n) -> Node:
    if not p:
        return None
    p.left = usun_wezly_powyzej_poziomu(p.left, n - 1)
    p.right = usun_wezly_powyzej_poziomu(p.right, n - 1)
    return None if n <= 0 else p  # jak powyzej n to usuwam


def usun_liscie(p) -> Node:
    if not p:
        return None
    if not p.left and not p.right:  # Czy liści
        return None
    p.left = usun_liscie(p.left)
    p.right = usun_liscie(p.right)
    return p


