<picture>
  <source srcset="../../srt/zbior_zadan/211.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_211.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_211.png" alt="zadanie 211">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def repair(p) -> Node:
    """bede tworzyl 2 lancuchy ktore potem zlacze"""
    odd_head = odd_tail = Node(0)
    even_head = even_tail = Node(0)

    while p:
        if p.val % 2 == 1:  # nieparzysta dołączam do odd_tail
            odd_tail.next = p
            odd_tail = odd_tail.next
        else:  # parzysta dołączam do even_tail
            even_tail.next = p
            even_tail = even_tail.next
        p = p.next

    # Doczepiam listę parzystą na koniec listy nieparzystej
    odd_tail.next = even_head.next
    even_tail.next = None
    return odd_head.next  # bez wartownika
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
