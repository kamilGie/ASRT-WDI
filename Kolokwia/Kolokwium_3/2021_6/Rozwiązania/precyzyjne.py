# ====================================================================================================>
# Zadanie 6, 20 stycznia 2022
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
#     def __init__(self, val):
#     self.val = val
#     self.next = None
#
# Lista zawierała wartości stanowiące kolejne wyrazy ciągu geometrycznego. Z wnętrza listy usunięto
# pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy),
# która uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu geometrycznego.
# Funkcja powinna zwrócić liczbę wstawionych elementów. Na przykład poniższa lista zostanie przekształcona:
# 4 -32 -128 -2048 −→ 4 -8 16 -32 64 -128 256 -512 1024 -2048 (zostanie zwrócona wartość 6)
# Można założyć, że lista wejściowa liczy więcej niż 2 elementy i każdy element
# listy jest liczbą całkowitą rózną od 0 (iloraz ciągu nie musi być całkowity).
# ====================================================================================================>
# Rozwiązane przez https://github.com/czyz-bartosz

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def nwd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def normalize(a: tuple):
    """Skraca ułamek przez nwd"""
    if a[1] < 0:
        a = (-a[0], -a[1])
    gcd = nwd(a[0], a[1])
    return (a[0] // gcd, a[1] // gcd)


def divide(a: tuple, b: tuple):
    """Dzieli ułamek (a/b) ÷ (c/d) == (a*d) / (b*c) oraz skaraca"""
    return normalize((a[0] * b[1], a[1] * b[0]))


def nwd_tuple(a: tuple, b: tuple):
    q1 = a[0] / a[1]
    if abs(q1) >= 1:
        while a != b:  # porownuje krotki
            if abs(a[0] / a[1]) >= abs(b[0] / b[1]):
                a = divide(a, b)
            else:
                b = divide(b, a)
    else:
        while a != b:
            if abs(a[0] / a[1]) >= abs(b[0] / b[1]):
                a = divide(b, a)
            else:
                a = divide(a, b)
    return a


def find_q(p):
    """Przechodzi po różnicach kolejnych elementów ciągu i wyznacza ich NWD"""
    q = divide((p.next.val, 1), (p.val, 1))
    while p.next:
        q = nwd_tuple(q, divide((p.next.val, 1), (p.val, 1)))
        p = p.next
    return q


def repair(p):
    q = find_q(p)

    inserted_count = 0
    while p.next:
        expected_value = p.val * q[0] / q[1]
        if (
            expected_value != p.next.val
        ):  # Jeśli nie dotarłem do wartości następnego elementu w ciągu
            p.next = Node(expected_value, p.next)  # Dodaję brakujący element do listy
            inserted_count += 1
        p = p.next
    return inserted_count
