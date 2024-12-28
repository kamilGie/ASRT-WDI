# ====================================================================================================>
# Zadanie 217
# Proszę napisać funkcję, która sprawdza czy dana liczba należy do drzewa BST. Funkcję
# proszę zrealizować jako funkcję rekurencyjną, a następnie jako funkcję bez użycia rekurencji.
# ====================================================================================================>



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}" 








def Zadanie_217_rek(p, val): ...



def Zadanie_217_iter(p, val): ...






if __name__ == "__main__":
    from testy217 import odpal_testy


    Zadanie_217_rek(Node(1, Node(2),Node(3)), int(input('Podaj val: ')))


    Zadanie_217_iter(Node(1, Node(2),Node(3)), int(input('Podaj val: ')))


    # odpal_testy()
