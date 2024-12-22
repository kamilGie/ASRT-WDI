# ====================================================================================================>
# Zadanie 211
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init (self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawiera wartości będące liczbami naturalnymi Proszę napisać funkcję repair(p), (p wskazuje na
# pierwszy element listy) która przekształca listę tak aby liczby parzyste znalazły się na końcu listy. Funk-
# cja powinna zwrócić wskazanie na przekształconą listę. Można założyć, że lista wejściowa liczy więcej niż 2
# elementy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def repair(p) -> Node: ...






if __name__ == "__main__":
    from testy211 import odpal_testy


    repair(Node(1, Node(2, Node(3))))


    # odpal_testy()
