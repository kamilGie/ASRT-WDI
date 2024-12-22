# ====================================================================================================>
# Zadanie 209
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
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def is_repairable(head, step):
    current_val = head.val
    while head.next:
        current_val += step
        if current_val == head.next.val:
            head = head.next
        elif (step > 0 and current_val > head.next.val) or (
            step < 0 and current_val < head.next.val
        ):
            return False
    return True


def repair(p):
    original_step = p.next.val - p.val

    divisor = 2
    step = original_step
    while not is_repairable(p, step):
        step = original_step / divisor
        divisor += 1

    inserted_count = 0
    while p.next:
        if p.val + step != p.next.val:
            p.next = Node(p.val + step, p.next)
            inserted_count += 1
        p = p.next
    return inserted_count


