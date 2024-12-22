# ====================================================================================================>
# Zadanie 186
# Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci jednokierunkowej
# listy. Napisy w łańcuchu są uporządkowane leksykograficznie. Proszę napisać stosowne definicje typów oraz
# funkcję dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis,
# funkcja powinna zwrócić wartość logiczną wskazującą, czy w wyniku operacji moc zbioru uległa zmianie.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_186(head, word) -> bool: ...






if __name__ == "__main__":
    from testy186 import odpal_testy


    Zadanie_186(Node(1, Node(2, Node(3))), int(input('Podaj word: ')))


    # odpal_testy()
