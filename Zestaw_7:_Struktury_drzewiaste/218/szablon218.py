# ====================================================================================================>
# Zadanie 218
# Proszę napisać funkcję, która wstawi liczbę do drzewa BST. Funkcję proszę zrealizować
# jako funkcję rekurencyjną, a następnie jako funkcję bez użycia rekurencji.
# ====================================================================================================>



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}" 








def Zadanie_218_rek(p, val) -> Node: ...



def Zadanie_218_iter(p, val) -> Node: ...






if __name__ == "__main__":
    from testy218 import odpal_testy


    Zadanie_218_rek(Node(1, Node(2),Node(3)), int(input('Podaj val: ')))


    Zadanie_218_iter(Node(1, Node(2),Node(3)), int(input('Podaj val: ')))


    # odpal_testy()
