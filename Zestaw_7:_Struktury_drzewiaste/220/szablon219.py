# ====================================================================================================>
# Zadanie 219
# Dane jest drzewo BST zbudowane z elementów ... Proszę zaimplementować funkcję zwra-
# cającą długość najdłuższej ścieżki kończącej się liściem, w której każdy węzeł ma tylko jednego syna.
# ====================================================================================================>



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}" 








def Zadanie_219(p, val=1): ...






if __name__ == "__main__":
    from testy219 import odpal_testy


    Zadanie_219(Node(1, Node(2),Node(3)), int(input('Podaj val: ')))


    # odpal_testy()
