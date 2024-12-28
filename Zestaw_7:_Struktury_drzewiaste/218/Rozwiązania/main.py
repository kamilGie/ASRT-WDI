# ====================================================================================================>
# Zadanie 218
# Proszę napisać funkcję, która wstawi liczbę do drzewa BST. Funkcję proszę zrealizować
# jako funkcję rekurencyjną, a następnie jako funkcję bez użycia rekurencji.
# ====================================================================================================>


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}"


def Zadanie_218_rek(p, val) -> Node:
    if not p:  # Dotarliśmy do liścia
        return Node(val)  # Nowy węzeł,

    if val < p.val:
        p.left = Zadanie_218_rek(p.left, val)  # Wstawiamy do lewego poddrzewa
    else:
        p.right = Zadanie_218_rek(p.right, val)  # Wstawiamy do prawego poddrzewa

    return p


def Zadanie_218_iter(p, val) -> Node:
    if not p:
        return Node(val)

    current = p
    while True:
        if val < current.val:
            if not current.left:
                current.left = Node(val)  # Nowy węzeł jako lewy potomek
                break
            current = current.left
        else:
            if not current.right:
                current.right = Node(val)  # Nowy węzeł jako prawy potomek
                break
            current = current.right

    return p


