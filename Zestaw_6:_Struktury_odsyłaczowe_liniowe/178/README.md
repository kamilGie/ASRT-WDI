<picture>
  <source srcset="../../srt/zbior_zadan/178.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_178.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_178.png" alt="zadanie 178">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(head):
    """odwraca kazdy wskaznik pokolei"""
    prev, curr = None, head
    while curr:
        next_node = curr.next  # Zachowaj wskaźnik na kolejny węzeł
        curr.next = prev  # Odwróć wskaźnik
        prev, curr = curr, next_node  # Przesuń wskaźniki
    return prev
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
