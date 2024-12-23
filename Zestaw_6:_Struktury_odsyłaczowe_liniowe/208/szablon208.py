# ====================================================================================================>
# Zadanie 208
# Proszę napisać funkcję, która usuwa z listy cyklicznej elementy, których klucz występuje
# dokładnie k razy. Do funkcji należy przekazać wskazanie na jeden z elementów listy, oraz liczbę k, funkcja
# powinna zwrócić informację czy usunięto jakieś elementy z listy.
# ====================================================================================================>
# zakladam ze lista jest cykliczna od poczatku  bez lancuchow przed cyklem


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_208(p, k)->bool: ...






if __name__ == "__main__":
    from testy208 import odpal_testy


    Zadanie_208(Node(1, Node(2, Node(3))), int(input('Podaj k: ')))


    # odpal_testy()
