# ====================================================================================================>
# Zadanie 189
# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
# jednokierunkowej,usuwa z niejwszystkie elementy, w których wartość klucza w zapisie trójkowym ma większą
# ilość jedynek niż dwójek.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_189(head)->Node: ...






if __name__ == "__main__":
    from testy189 import odpal_testy


    Zadanie_189(Node(1, Node(2, Node(3))))


    # odpal_testy()
