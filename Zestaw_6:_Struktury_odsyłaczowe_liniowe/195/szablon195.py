# ====================================================================================================>
# Zadanie 195
# Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą.
# Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia
# jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")








def Zadanie_195(current)->Node: ...






if __name__ == "__main__":
    from testy195 import odpal_testy


    Zadanie_195(int(input('Podaj current: ')))


    # odpal_testy()
