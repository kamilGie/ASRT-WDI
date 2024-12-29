# ====================================================================================================>
# Zadanie B6, 19.01.2023
# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola key i next, której węzły
# przechowują liczby całkowite. Proszę napisać funkcję separate(p) która rozdziela listę cykliczną na dwie
# listy cykliczne. Pierwsza powinna zawierać klucze parzyste dodatnie, druga klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać wskaźniki na listę z danymi. Funkcja
# powinna zwrócić wskaźniki na powstałe listy oraz liczbę usuniętych elementów.
# ====================================================================================================>


class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next: Node | None = next

    def __str__(self):
        result = []
        start = self
        while start:
            result.append(str(start.key))
            start = start.next
            if start == self:  # Zakończenie cyklu
                result.append("(cykl)")
                break
        return " -> ".join(result)


def separate(p):
    # Tworzę nowe listy zaczynające się od wartowników
    positive_even_head = positive_even_tail = Node(None)
    negative_odd_head = negative_odd_tail = Node(None)
    removed_count = 0

    # Odłączam, aby usunąć cykl
    current = p.next
    p.next = None

    while current:
        # Odłączam bieżący węzeł
        next_node = current.next
        current.next = None

        # Decyduję, co zrobić z odłączonym węzłem
        if current.key > 0 and current.key % 2 == 0:  # Dodatnie parzyste
            positive_even_tail.next = current
            positive_even_tail = current
        elif current.key < 0 and current.key % 2 == 1:  # Ujemne nieparzyste
            negative_odd_tail.next = current
            negative_odd_tail = current
        else:  # Węzeł do usunięcia
            removed_count += 1

        current = next_node

    # Tworzę cykliczne listy
    positive_even_tail.next = positive_even_head.next
    negative_odd_tail.next = negative_odd_head.next

    # Zwracam listy bez wartowników i liczbę usuniętych węzłów
    return positive_even_head.next, negative_odd_head.next, removed_count


