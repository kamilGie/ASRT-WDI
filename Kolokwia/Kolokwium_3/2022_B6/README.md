<picture>
  <source srcset="../../srt/zbior_zadan/2022_B6.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_2022_B6.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_2022_B6.png" alt="zadanie 2022_B6">
</picture>

```python
class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


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
```
