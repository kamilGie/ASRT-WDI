# ====================================================================================================>
# Zadanie 215
# Proszę napisać następujące funkcje:
# 1. Funkcja, która usunie wszystkie węzły drzewa.
# 2. Funkcja, która usunie węzły powyżej n-tego poziomu.
# 3. Funkcja, która usunie wszystkie aktualne liście drzewa.
# ====================================================================================================>



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}" 








def usun_wszystkie_wezly(p): ...



def usun_wezly_powyzej_poziomu(p, n) -> Node: ...



def usun_liscie(p) -> Node: ...






if __name__ == "__main__":
    from testy215 import odpal_testy


    usun_wszystkie_wezly(Node(1, Node(2),Node(3)))


    usun_wezly_powyzej_poziomu(Node(1, Node(2),Node(3)), int(input('Podaj n: ')))


    usun_liscie(Node(1, Node(2),Node(3)))


    # odpal_testy()
