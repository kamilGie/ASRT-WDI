# ====================================================================================================>
# Zadanie 206
# Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w liście ułożone są
# według rosnących potęg. Proszę napisać funkcję obliczającą różnicę dwóch dowolnych wielomianów. Wielo-
# mianyreprezentowane są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo utworzonej
# listy reprezentującej wielomian wynikowy. Listy wejściowe powinny pozostać niezmienione.
# ====================================================================================================>
# p - q


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_206(p, q)->Node ...






if __name__ == "__main__":
    from testy206 import odpal_testy


    Zadanie_206(Node(1, Node(2, Node(3))), Node(1, Node(2, Node(3))))


    # odpal_testy()
