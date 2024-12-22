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
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_186(head, word) -> bool:
    current = Node("", head)  # Węzeł pomocniczy na początku listy

    while current.next and current.next.val < word:
        current = current.next

    if current.next and current.next.val == word:
        return False  # istnieje w zbiorze

    # Wstawianie nowego węzła z napisem
    current.next = Node(word, current.next)
    return True


