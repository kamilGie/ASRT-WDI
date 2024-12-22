# ====================================================================================================>
# Zadanie 180
# Proszę napisać funkcję wstawiającą na koniec listy nowy element.
# Do funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą wartość.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def push_back(p, val) -> Node: ...






if __name__ == "__main__":
    from testy180 import odpal_testy


    push_back(Node(1, Node(2, Node(3))), int(input('Podaj val: ')))


    # odpal_testy()
