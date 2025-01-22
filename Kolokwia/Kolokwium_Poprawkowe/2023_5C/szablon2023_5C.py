# ====================================================================================================>
# Zadanie 5C, 2024-02-06
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
#  def init(self, val, next=None):
#  self.val = val
#  self.next = next
# Lista zawiera wartości będące liczbami naturalnymi. Proszę napisać funkcję divide(p) (p wskazuje
# na pierwszy element listy), która rozdziela listę na dwie listy. W pierwszej powinny się znaleźć
# liczby, które są wielokrotnością (co najmniej dwukrotnością) kwadratu dowolnej liczby pierwszej, a w
# drugiej pozostałe liczby. Względny porządek w powstałych listach nie powinien ulec zmianie. Funkcja
# powinna zwrócić wskazania do obu list.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def divide(p): ...


if __name__ == "__main__":
    from testy2023_5C import odpal_testy, podpowiedz

    divide(Node(1, Node(8, Node(2, Node(16)))))  # return  (1->2 , 8->16)

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    odpal_testy()
