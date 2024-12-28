# ====================================================================================================>
# Zadanie 220
# Proszę napisać funkcję, która dla drzewa BST zwraca wysokość najwyższego poddrzewa
# będącego listą.
# ====================================================================================================>
# to samo co 219


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}"

def Zadanie_219(p, val=1):
    if not p:  # Pusty węzeł
        return val

    if p.right and p.left:  # Węzeł ma dwóch synów
        return max(Zadanie_219(p.left), Zadanie_219(p.right))

    if p.right:  # Węzeł ma tylko prawego syna
        return Zadanie_219(p.right, val + 1)

    if p.left:  # Węzeł ma tylko lewego syna
        return Zadanie_219(p.left, val + 1)

    return val  # Węzeł liścia


