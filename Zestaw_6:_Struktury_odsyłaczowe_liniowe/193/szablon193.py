# ====================================================================================================>
# Zadanie 193
# Elementy w liście są uporządkowane według wartości klucza. Proszę napisać funkcję usuwającą z listy
# elementy o nie unikalnym kluczu. Do funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_193(head)->int: ...






if __name__ == "__main__":
    from testy193 import odpal_testy


    Zadanie_193(Node(1, Node(2, Node(3))))


    # odpal_testy()
