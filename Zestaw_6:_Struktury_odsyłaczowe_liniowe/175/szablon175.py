# ====================================================================================================>
# Zadanie 175
# Proszę zaimplementować zbiór mnogościowy liczb naturalnych korzystając ze struktury
# listy odsyłaczowej.
# • czy element należy do zbioru
# • wstawienie elementu do zbioru
# • usunięcie elementu ze zbioru
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")










def contains(head, value) -> bool: ...



def insert(head, value) -> Node: ...



def delete_node(head, value) -> Node: ...








if __name__ == "__main__":
    from testy175 import odpal_testy


    contains(Node(1, Node(2, Node(3))), int(input('Podaj value: ')))


    insert(Node(1, Node(2, Node(3))), int(input('Podaj value: ')))


    delete_node(Node(1, Node(2, Node(3))), int(input('Podaj value: ')))


    # odpal_testy()
