<picture>
  <source srcset="../../srt/zbior_zadan/227.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_227.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_227.png" alt="zadanie 227">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


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
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
