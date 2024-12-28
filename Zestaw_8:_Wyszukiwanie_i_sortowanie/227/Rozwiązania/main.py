# ====================================================================================================>
# Zadanie 227
# Dana jest lista odsyłaczowa przechowująca liczby całkowite. Proszę napisać funkcję wsta-
# wiającą istniejący element do posortowanej listy, a następnie zrealizować funkcję sortowania przez wstawianie
# (insertion sort).
# ====================================================================================================>

from math import inf


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def insert_to_sorted(p, val):
    head = Node(-inf, p)  # Minimalna wartość jako wartownik

    current = head
    while current.next and current.next.val < val:
        current = current.next

    current.next = Node(val, current.next)

    return head.next  # bez wartownika


def sort_by_insertion_sort(p):
    sorted_head = None

    while p:
        sorted_head = insert_to_sorted(sorted_head, p.val)
        p = p.next

    return sorted_head


