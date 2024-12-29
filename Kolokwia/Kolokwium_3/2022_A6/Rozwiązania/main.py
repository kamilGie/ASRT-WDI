# ====================================================================================================>
# Zadanie A6, 17.01.2023
# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola val i next, której węzły
# przechowują liczby naturalne. Liczby przechowywane w liście spełniają warunek ”łączności”, tzn. dla każdego węzła ostatnia cyfra liczby jest identyczna z pierwszą cyfrą liczby z następnego węzła. Proszę napisać
# funkcję insert(p, n), która wstawia do listy wskazywanej przez wskaźnik p, liczbę n, metodą zastąpienia
# co najmniej dwóch elementów jednym zawierającym wstawioną liczbę. Po wstawieniu nowej liczby nadal
# zachowany powinien być warunek ”łączności”. Funkcja powinna zwrócić o ile skrócona została lista albo
# wartość 0 gdy elementu nie można wstawić do listy.
# Na przykład dla listy zawierającej elementy: 2023 31 17 703 37 707 72 29 902
# po wstawieniu liczby 303 lista może wyglądać następująco: 2023 303 37 707 72 29 902
# Funkcja powinna zwrócić wartość 2.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next: Node | None = next

    def __str__(self):
        result = []
        start = self
        while start:
            result.append(str(start.val))
            start = start.next
            if start == self:  # Zakończenie cyklu
                result.append("(cykl)")
                break
        return " -> ".join(result)


def first_digit(x):
    while x >= 10:
        x //= 10
    return x


def last_digit(x):
    return x % 10


def insert(p, n):
    head = p

    while True:
        # Szukamy początku (gdzie ostatnia cyfra zgadza się z pierwszą cyfrą n)
        if last_digit(head.val) == first_digit(n):
            start = head
            current = start.next
            length = 0

            # Szukamy końca (gdzie pierwsza cyfra zgadza się z ostatnią cyfrą n)
            while current != start:
                length += 1
                if first_digit(current.val) == last_digit(n):
                    # Jeśli długość > 2, wstawiamy i zwracamy długość
                    if length > 2:
                        start.next = Node(n, current)
                        return length - 2  # minus koniec ktorego nie usuwamy oraz ona sama
                current = current.next

        head = head.next
        if head == p:  # Jeśli wróciliśmy do początku listy, kończymy
            break

    return 0


