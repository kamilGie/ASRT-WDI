# ====================================================================================================>
# Zadanie 204
# Dane są dwie nie puste listy, z których każda zawiera nie powtarzające się elementy. Elementy
# wpierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej kolejności.Proszę
# napisać funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane elementy będą stanowić
# sumę mnogościową elementów z list wejściowych. Do funkcji należy przekazać wskazania na obie listy, funkcja
# powinna zwrócić wskazanie na listę wynikową. Na przykład dla list:
# 2→3→5→7→11
# 8→2→7→4
# powinna pozostać lista:
# 2→3→4→5→7→8→11
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_204(p, q): ...






if __name__ == "__main__":
    from testy204 import odpal_testy


    Zadanie_204(Node(1, Node(2, Node(3))), Node(1, Node(2, Node(3))))


    # odpal_testy()
