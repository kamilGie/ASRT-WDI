# ====================================================================================================>
# Zadanie 194
# Dana jest lista zawierająca ciąg obu stronnie domkniętych przedziałów. Krańce przedziałów
# określa uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję redukującą
# liczbę elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany
# do listy: [13,19] [2,6] [7,12]
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_194(head)->Node: ...






if __name__ == "__main__":
    from testy194 import odpal_testy


    Zadanie_194(Node(1, Node(2, Node(3))))


    # odpal_testy()
