# ====================================================================================================>
# Zadanie 176
# Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy
# funkcje:
# • inicjalizującą tablicę,
# • zwracającą wartość elementu o indeksie n,
# • podstawiającą wartość value pod indeks n.
# ====================================================================================================>
# Tablica rzadka przechowa tylko wartości  wraz z ich indeksami, np. w postaci listy:
# Przykład
# Zwykła tablica:
# [None,None,5,None,None,None,8,None,None,3]
# tablica rzadka
# [(2,5),(6,8),(9,3)]


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def set_value(p, n, v) -> Node: ...



def get_value(p, n) -> Node | None: ...



def initialize_set(p) -> Node: ...






if __name__ == "__main__":
    from testy176 import odpal_testy


    p = initialize_set(Node(1, Node(2, Node(3))))

    set_value(p, int(input('Podaj n: ')), int(input('Podaj v: ')))


    get_value(p, int(input('Podaj n: ')))



    # odpal_testy()
