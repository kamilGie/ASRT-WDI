# ====================================================================================================>
# Zadanie 216
# Proszę napisać funkcję, która sprawdza czy dane drzewo jest poprawnym drzewem BST.
# ====================================================================================================>



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}" 








def Zadanie_216(p): ...






if __name__ == "__main__":
    from testy216 import odpal_testy


    Zadanie_216(Node(1, Node(2),Node(3)))


    # odpal_testy()
