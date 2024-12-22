# ====================================================================================================>
# Zadanie 173
# wypisywanie elementów łańcucha
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



def wypis(p): ...




if __name__ == "__main__":
    from testy173 import odpal_testy


    wypis(Node(1, Node(2, Node(3))))


    # odpal_testy()
