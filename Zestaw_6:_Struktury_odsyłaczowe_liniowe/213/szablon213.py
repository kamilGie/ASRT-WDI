# ====================================================================================================>
# Zadanie 213
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init(self,val,next=None):
# ....self.val = val
# ....self.next = next
# Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto pewną
# liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która uzupeł-
# nia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja powinna
# zwrócić liczbę wstawionych elementów. Można założyć, że lista wejściowa liczy więcej niż 2 elementy.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def repair(p)->int: ...






if __name__ == "__main__":
    from testy213 import odpal_testy


    repair(Node(1, Node(2, Node(3))))


    # odpal_testy()
